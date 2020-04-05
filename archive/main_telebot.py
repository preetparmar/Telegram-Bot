# Importing Libraries
import telebot
import logging

# Importing Custom Functions
from credentials import telegram_key
from my_functions import all_functions

# Defining Variables


# Logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def main():
    # Initializing the bot
    bot = telebot.TeleBot(telegram_key)
    all_functions(bot)
    bot.polling()
    

if __name__ == '__main__':
    main()

