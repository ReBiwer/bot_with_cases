from telebot.types import Message
import requests
import json
from config_data.config import *
from loader import bot
from states.getting_weather import GettingWeather


@bot.message_handler(commands=["find_weather"])
def get_weather(message: Message):
    bot.set_state(message.from_user.id, GettingWeather.city, message.chat.id)
    bot.send_message(message.chat.id, 'Введите город где вы хотите узнать погоду')


@bot.message_handler(state=GettingWeather.city)
def put_weather(message: Message):
    GettingWeather.city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={GettingWeather.city}&appid={RAPID_API_KEY}&units=metric')
    if res.status_code == 200:
        data = json.loads(res.text)
        temp_in_city = data["main"]["temp"]
        bot.reply_to(message, f'Погода в городе {GettingWeather.city.capitalize()}: {temp_in_city}')
        image = 'sunny_weather.jpg' if temp_in_city < 5.0 else 'sun_weather.jpg'
        with open('images/' + image, 'rb') as file:
            bot.send_photo(message.chat.id, file)
    else:
        bot.send_message(message.chat.id, 'Город указан не верно')