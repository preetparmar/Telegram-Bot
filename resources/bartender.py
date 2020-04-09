import requests

def get_cocktail(update, context):
    name = update.message.text[11:]
    if name == '':
        URL = 'https://www.thecocktaildb.com/api/json/v1/1/random.php'
    else:
        URL = f'https://www.thecocktaildb.com/api/json/v1/1/search.php?s={name}'

    data = requests.get(URL).json()['drinks']
    
    if data:
        cocktail, drink_image = get_cocktail_details(URL, data[0])
        context.bot.send_message(chat_id=update.effective_chat.id, text=cocktail)
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=drink_image)
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text='No cocktail found')

def get_ingredient(update, context):
    name = update.message.text[14:]
    URL = f'https://www.thecocktaildb.com/api/json/v1/1/search.php?i={name}'
    data = requests.get(URL).json()['ingredients']
    if data:
        ingredient_name = data[0]['strIngredient']
        ingredient_desc = data[0]['strDescription']
        ingredient_details = f'Name: {ingredient_name}\nDescription: {ingredient_desc}'
        context.bot.send_message(chat_id=update.effective_chat.id, text=ingredient_details)
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text='No such ingredient found')


def search_cocktail(update, context):
    name = update.message.text[17:]
    URL = f'https://www.thecocktaildb.com/api/json/v1/1/search.php?f={name}'
    data = requests.get(URL).json()['drinks']
    if data:
        all_drinks = ' | '.join([drink['strDrink'] for drink in data])
        context.bot.send_message(chat_id=update.effective_chat.id, text=all_drinks)
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text='No such cocktail found.\nTry searching something else.')


def get_cocktail_details(URL, data):
    str_ingredients = [f'strIngredient{i}' for i in range(1, 16)]
    str_measures = [f'strMeasure{i}' for i in range(1, 16)]

    data = requests.get(URL).json()['drinks'][0]
    drink_name = data['strDrink']
    drink_category = data['strCategory']
    drink_image = data['strDrinkThumb']
    alcoholic = data['strAlcoholic']
    instructions = data['strInstructions']
    ingredients = [data[ingredient] for ingredient in str_ingredients if data[ingredient] is not None]
    measures = [data[measure] for measure in str_measures if data[measure] is not None]
    ingredient_measure = ''
    for ingredient, measure in zip(ingredients, measures):
        ingredient_measure += f'{ingredient} : {measure}\n'

    cocktail = f'Name: {drink_name}\nCategory: {drink_category}\nType: {alcoholic}\n\nIngredients:\n{ingredient_measure}\nInstructions: {instructions}'
    return cocktail, drink_image

