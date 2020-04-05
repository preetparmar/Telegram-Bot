# Importing Libraries
import json
import requests


def aww():
    URL = 'https://dog.ceo/api/breeds/image/random'
    r = requests.get(URL)
    if r.status_code == 200:
        return r.json()['message']
    else:
        return None


def send_dog_photo(update, context):
    URL = 'https://dog.ceo/api/breeds/image/random'
    r = requests.get(URL)
    if r.status_code == 200:
        photo_url = r.json()['message']
    else:
        return None
    context.bot.send_photo(update.effective_chat.id, photo=photo_url)
