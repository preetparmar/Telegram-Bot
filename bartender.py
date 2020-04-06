import requests
import telegram

def get_random_cocktail(update, context):
    str_ingredients = [f'strIngredient{i}' for i in range(1, 16)]
    str_measures = [f'strMeasure{i}' for i in range(1, 16)]
    URL = 'https://www.thecocktaildb.com/api/json/v1/1/random.php'

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

    context.bot.send_message(chat_id=update.effective_chat.id, text=cocktail)
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=drink_image)
