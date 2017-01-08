import config
from telegram.ext import Updater, CommandHandler
import logging
from irish_dictionary import irish_dictionary

updater = Updater(token=config.TOKEN)
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)



def caps(bot, update, args):
    print(args)
    text_caps = ' '.join(args).upper()
    bot.sendMessage(chat_id=update.message.chat_id, text=text_caps)


def irish(bot, update, args):
    if not args:
        bot.sendMessage(chat_id=update.message.chat_id, text="Please input a word to translate")
        return
    entry = args[0]
    entries, suggestions, wordlist, grammatical = irish_dictionary(entry, 'irish', 'english')
    if len(entries) == 0:
        bot.sendMessage(chat_id=update.message.chat_id, text="Word not found in the Foclóir Gaeilge-Béarla")
    for defi in entries:
        if len(defi) > 4096:
            defi = defi[:4095]
        bot.sendMessage(chat_id=update.message.chat_id, text=defi)

def english(bot, update, args):
    if not args:
        bot.sendMessage(chat_id=update.message.chat_id, text="Please input a word to translate")
        return
    entry = args[0]
    entries, suggestions, wordlist, grammatical = irish_dictionary(entry, 'english', 'english')
    if len(entries) == 0:
        bot.sendMessage(chat_id=update.message.chat_id, text="Word not found in the English-Irish Dictionary")
    for defi in entries:
        if len(defi) > 4096:
            defi = defi[:4095]
        bot.sendMessage(chat_id=update.message.chat_id, text=defi)


def error(bot, update, error):
    logger.warn('Update %s caused error "%s"' % (update, error))

caps_handler = CommandHandler('caps', caps, pass_args=True)
irish_handler = CommandHandler('ga', irish, pass_args=True)
english_handler = CommandHandler('en', english, pass_args=True)



dispatcher.add_handler(caps_handler)
dispatcher.add_handler(irish_handler)
dispatcher.add_handler(english_handler)
dispatcher.add_error_handler(error)

updater.start_polling()
