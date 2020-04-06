import requests

def send_joke(update, context):
    url = "https://joke3.p.rapidapi.com/v1/joke"
    querystring = {"nsfw":"true"}
    headers = {
        'x-rapidapi-host': "joke3.p.rapidapi.com",
        'x-rapidapi-key': "835e43cd47msh7bd57988c0e031bp1c9130jsn7007aed3b0c8"
        }

    response = requests.request("GET", url, headers=headers, params=querystring).json()
    joke = response['content']
    context.bot.send_message(chat_id=update.effective_chat.id, text=joke)
