# Telegram-Bot

I have created my own Telegram Bot using a [python wrapper](https://github.com/python-telegram-bot/python-telegram-bot)
<!-- ![PrtPrmr_Bot](https://github.com/preetparmar/Telegram-Bot/blob/master/screenshots/test.png) -->

## Getting Started:
- Search for `PrtPrmr_Bot` in your **Telegram App** on your mobile/windows/mac
    - *Please replace `PrtPrmr_Bot` with your bot name if you are planning on replicating the code*
- Start interacting with the Bot. It's that easy!

## Some Functionalities:
**Definition and example of a word**
- Command: `def`
- Usage: **/def** *word*
- If an example for the word is available then the command returns an example as well
- Example: 
    - */def intense*
    - *Definition: of extreme force, degree, or strength<br/>Example: the job demands intense concentration*

**Weather for the given place**
- Command: `w`
- For the purpose of this, I have decided to use Dark Sky Weather API.
    - Dark Sky API requires *Latitude* and *Longitude*
    - In order to get the Latitude and Longitude, I am using Google's Geo-Coding API
    - The place is passed to Google's Geo-Coding API, which returns Latitude and Longitude of the given place
    - The Latitude and Longitude is then passed to Dark Sky Weather API to get the weather
- Added `InlineKeyboard` functionality to select Celsius and Fahrenheit units of temperature
- Usage: **/w** *place*
- Example:
    - */w boston*
    - *Currently the temperature is 8°C<br/>Summary: Mostly cloudy throughout the day.<br/>Today it will vary from 8°C to 15°C*

**Get a random cocktail recipe**
- Command: `cocktail`
- Usage: **/cocktail**
- Example:
    - */cocktail*
    - *Name: Harvey Wallbanger<br/>Category: Ordinary Drink<br/>Type: Alcoholic<br/>Ingredients:<br/>Vodka : 1 oz<br/>Galliano : 1/2 oz<br/>Orange juice : 4 oz<br/>Instructions: Stir the vodka and orange juice with ice in the glass, then float the Galliano on top. Garnish and serve.*

**Get a random meme**
- Usage: **/ha** | **/haha** | **/hahaha**
    - Added a `regex` functionality to the command so you can use `ha` as a command as many times

**Get a random cute dog photo! <3 Aww!!!**
- Usage: **/aw** | **/aww** | **/awww**
    - Added a `regex` functionality, so that you can use the command `aw` with any numbers *w* follwing `aw`

**Get a random joke :D**
- Command: `joke`
- Usage: **/joke**
- Provides a random joke everytime
- *Will add functionality to toggle `NSFW` feature*

**Handling Unknown Commands**
- If a command is given which is currently not available, then you will get a reply *Invalid Command*

## Requirements:
- Create a `credentials.py` file
- Add variables in the `credentials.py` file:
    - `telegram_key`: *Your Telegram Bot Token*
    - `dark_sky_key`: *Dark Sky Weather API*
    - `geocoding_key`: *Google's Geo-Coding API*
    - `oxford_id`: *Oxford Dictionary API ID*
    - `oxford_key`: *Oxford Dictionary API Key*
- The script uses API from:
    - [Oxford Dictionary API](https://developer.oxforddictionaries.com/) - *Requires Log In*
    - [Dark Sky API](https://darksky.net/dev) - *Requires Log In*
    - [Google Geo-Coding API](https://developers.google.com/maps/documentation/geocoding/start) - *Requires Log In*
    - [meme api](https://meme-api.herokuapp.com/) - *Open Source*
    - [dog api](https://dog.ceo/dog-api/) - *Open Source*

<!-- ## Some functions in the Pipeline:
- Get real time location for MBTA Boston.
- Store interaction and user data into database -->

If you have any suggestions or just want to chat, feel free to reach me preetparmar@outlook.com