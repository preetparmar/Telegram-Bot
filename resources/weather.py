# Importing Libraries
import requests
import json
from datetime import datetime as dt
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

# Importing Custom Varaibles
from credentials import geocoding_key, dark_sky_key, words_api_key


def get_long_lat(place:str):
    """ Search for Lattitude and Longitude of the given place """
    updated_place = place.replace(' ', '+')
    url = f'https://maps.googleapis.com/maps/api/geocode/json?address={updated_place}&key={geocoding_key}'
    response = requests.get(url).json()
    latitude = response['results'][0]['geometry']['location']['lat']
    longitude = response['results'][0]['geometry']['location']['lng']
    return latitude, longitude


def f_to_c(temp):
    """ Converts the Fahrenheit to Celsius """
    return round((temp - 32) * 5 / 9)


def get_weather(place, units='c'):
    """ Gets Weather and Summary for the given place """
    
    latitude, longitude = get_long_lat(place)
    url = f'https://api.darksky.net/forecast/{dark_sky_key}/{latitude},{longitude}'
    response = requests.get(url).json()
    if units == 'c':
        # current_app_temp = f_to_c(round(response['currently']['apparentTemperature']))
        current_temp = f_to_c(round(response['currently']['temperature']))
        min_temp = f_to_c(round(response['daily']['data'][0]['temperatureMin']))
        max_temp = f_to_c(round(response['daily']['data'][0]['temperatureMax']))
        # current_time = response['currently']['time']
        # current_wind_speed = response['currently']['windSpeed']
        daily_summary = response['daily']['data'][0]['summary']
        weather_string = f'Currently the temperature is {current_temp}{chr(176)}C \n'\
        f'Summary: {daily_summary} \n'\
        f'Today it will vary from {min_temp}{chr(176)}C to {max_temp}{chr(176)}C'
    elif units == 'f':
        # current_app_temp = round(response['currently']['apparentTemperature'])
        current_temp = round(response['currently']['temperature'])
        min_temp = round(response['daily']['data'][0]['temperatureMin'])
        max_temp = round(response['daily']['data'][0]['temperatureMax'])
        # current_time = response['currently']['time']
        # current_wind_speed = response['currently']['windSpeed']
        daily_summary = response['daily']['data'][0]['summary']
        weather_string = f'Currently the temperature is {current_temp}{chr(176)}F \n'\
        f'Summary: {daily_summary} \n'\
        f'Today it will vary from {min_temp}{chr(176)}F to {max_temp}{chr(176)}F'

    return weather_string


def get_place(update, context):
    global place
    place = update.message.text[3:]
    keyboard = [
        [
            InlineKeyboardButton("Celsius", callback_data='c'),
            InlineKeyboardButton("Fahrenheit", callback_data='f')
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Please choose:', reply_markup=reply_markup)
    return place


def send_weather(update, context):
    query = update.callback_query
    query.answer()
    unit = query.data
    weather = get_weather(place, unit)
    context.bot.send_message(chat_id=update.effective_chat.id, text=weather)
