"""
All my custom functions which are used in the Telegram Bot
"""

def welcome(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Welcome to my Bot')

def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Invalid Command!')

