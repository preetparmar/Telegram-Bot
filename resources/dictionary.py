# Import Libraries
import json
import requests
from credentials import oxford_id, oxford_key
from credentials import words_api_key

def get_definition(term: str) -> str:
    """ Search for the definition of the given term """

    url = f"https://od-api.oxforddictionaries.com/api/v2/entries/en-us/{term.lower()}?strictMatch=false"
    r = requests.get(url, headers = {'app_id': oxford_id, 'app_key': oxford_key})
    if r.status_code == 200:
        result = r.json()
        definition = result['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions'][0]
        try:
            example = result['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['examples'][0]['text']
        except:
            example = None
        if example is not None:
            return f'Definition: {definition}\n\nExample: {example}'
        else:
            return f'Definition: {definition}'
    elif r.status_code == 404:
        return "Word can't be found!\nPlease check your spelling"

def send_definition(update, context):
    text = get_definition(update.message.text[4:])
    context.bot.send_message(chat_id=update.effective_chat.id, text=text)