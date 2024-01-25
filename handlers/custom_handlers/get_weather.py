from telebot.types import Message, ReplyKeyboardRemove
import requests
import json
from config_data.config import *
from loader import bot
from states.getting_weather import GettingWeather
from keyboards.inline.yes_no_inline import keyboard_inline


@bot.message_handler(commands=["find_weather"])
def get_weather(message: Message):
    bot.set_state(message.from_user.id, GettingWeather.city, message.chat.id)
    bot.send_message(message.chat.id, 'Введите город где вы хотите узнать погоду')


@bot.callback_query_handler(func=lambda call: call.data == 'да')
def get_weather_again(call):
    message = call.message
    bot.set_state(message.from_user.id, GettingWeather.city, message.chat.id)
    bot.send_message(message.chat.id, message.text)
    bot.send_message(message.chat.id, 'Введите город где вы хотите узнать погоду')


@bot.message_handler(state=GettingWeather.city)
def put_weather(message: Message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={RAPID_API_KEY}&units=metric')
    if res.status_code == 200:
        data = json.loads(res.text)
        temp_in_city = data["main"]["temp"]
        bot.reply_to(message, f'Погода в городе {city.capitalize()}: {temp_in_city}')
        image = 'sunny_weather.jpg' if temp_in_city < 5.0 else 'sun_weather.jpg'
        with open('images/' + image, 'rb') as file:
            bot.send_photo(message.chat.id, file)
        bot.delete_state(message.from_user.id, message.chat.id)

        bot.send_message(message.chat.id, 'Хотите узнать погоду в другом городе?',
                         reply_markup=keyboard_inline('да', 'нет'))
    else:
        bot.send_message(message.chat.id, 'Город указан не верно')


@bot.callback_query_handler(func=lambda call: call.data == 'нет')
def restart(call):
    message = call.message
    bot.send_message(message.chat.id, 'Выберите нужную команду в меню')
