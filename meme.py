# Importing Libraries
import json
import requests


def haha(update, context):
    URL = 'https://meme-api.herokuapp.com/gimme'
    r = requests.get(URL)
    if r.status_code == 200:
        photo_url = r.json()['url']
    else:
        return None
    context.bot.send_photo(update.effective_chat.id, photo=photo_url)
