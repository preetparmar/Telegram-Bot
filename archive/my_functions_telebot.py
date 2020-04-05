# Importing Custom Functions
from weather import get_weather
from dictionary import get_definition
from random_dog import aww

def all_functions(bot):

    # Welcome
    @bot.message_handler(commands=['start', 'help'])
    def send_welcome(message):
        bot.reply_to(message=message, text="Howdy, how are you doing?")

    #GIF
    @bot.message_handler(commands=['gif'])
    def get_gif(message):
        print(message.text[5:])

    # Get Definitions
    @bot.message_handler(commands=['def'])
    def define_this(message):
        word = message.text[5:]
        definition = get_definition(word)
        bot.reply_to(message, definition)

    # Get Weather
    @bot.message_handler(commands=['w'])
    def find_weather(message):
        place = message.text[3:]
        weather = get_weather(place)
        bot.reply_to(message, weather)

    # Get Dog Picture
    @bot.message_handler(regexp='a[w]+')
    def get_dog_photo(message):
        bot.reply_to(message, 'Aww')
        photo = aww()
        print(photo)
        bot.send_photo(message, photo=photo)
    
    @bot.message_handler(commands=['test'])
    def test(message):
        bot.reply_to(message, text=message.entities)
    