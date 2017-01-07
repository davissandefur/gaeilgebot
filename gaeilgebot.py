import config
from telegram.ext import Updater, CommandHandler
import logging
from irish_dictionary import irish_dictionary

updater = Updater(token=config.TOKEN)
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def start(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")

def caps(bot, update, args):
    print(args)
    text_caps = ' '.join(args).upper()
    bot.sendMessage(chat_id=update.message.chat_id, text=text_caps)


def irish(bot, update, args):
    if not args:
        bot.sendMessage(chat_id=update.message.chat_id, text="Please input a word to translate")
        return
    entry = args[0]
    entries, suggestions, wordlist, grammatical = irish_dictionary(entry, 'irish', 'gaeilge')
    for defi in entries:
        bot.sendMessage(chat_id=update.message.chat_id, text=defi)

def english(bot, update, args):
    if not args:
        bot.sendMessage(chat_id=update.message.chat_id, text="Please input a word to translate")
        return
    entry = args[0]
    entries, suggestions, wordlist, grammatical = irish_dictionary(entry, 'english', 'english')
    for defi in entries:
        bot.sendMessage(chat_id=update.message.chat_id, text=defi)


start_handler = CommandHandler('start',start)
caps_handler = CommandHandler('caps', caps, pass_args=True)
irish_handler = CommandHandler('ga', irish, pass_args=True)
english_handler = CommandHandler('en', english, pass_args=True)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(caps_handler)
dispatcher.add_handler(irish_handler)
dispatcher.add_handler(english_handler)

updater.start_polling()
