# Importing Libraries
from telegram.ext import Updater
from credentials import telegram_key
from telegram.ext import CommandHandler, CallbackQueryHandler
from telegram.ext import MessageHandler, Filters, RegexHandler

# Importing Custom Functions
from telegram_functions import welcome, unknown
from random_dog import send_dog_photo
from dictionary import send_definition
from weather import get_place, send_weather
from meme import haha

def add_handlers(dp):
    dp.add_handler(handler=CommandHandler(command='start', callback=welcome))
    dp.add_handler(handler=MessageHandler(filters=Filters.command & Filters.regex('a[w]+'), callback=send_dog_photo))
    dp.add_handler(handler=CommandHandler(command='def', callback=send_definition))
    dp.add_handler(handler=CommandHandler(command='w', callback=get_place))
    dp.add_handler(handler=CallbackQueryHandler(callback=send_weather))
    dp.add_handler(handler=MessageHandler(filters=Filters.command & Filters.regex('[ha]+'), callback=haha))
    dp.add_handler(handler=MessageHandler(filters=Filters.command, callback=unknown))

def main():
    updater = Updater(token=telegram_key, use_context=True)
    dp = updater.dispatcher
    add_handlers(dp)
    updater.start_polling()
    # updater.idle()

if __name__ == '__main__':
    main()

