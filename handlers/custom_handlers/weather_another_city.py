from telebot.types import Message, CallbackQuery
import requests
import json
from config_data.config import *
from loader import bot
from states.getting_weather import GettingWeather
from keyboards.inline.yes_no_inline import yes_no_keyboard_inline
from handlers.custom_func.weather_detection import weather_another_city_detection
from handlers.custom_func.get_photo_dog import get_photo_dog


@bot.callback_query_handler(func=lambda call: call.data == 'another_city')
def weather_another_city(call: CallbackQuery):
    message = call.message
    bot.set_state(GettingWeather.id_user, GettingWeather.another_city)
    bot.send_message(message.chat.id, 'Введите город где вы хотите узнать погоду')


@bot.message_handler(state=GettingWeather.another_city)
def put_weather(message: Message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY_weather}'
                       f'&units=metric&lang=ru')
    if res.status_code == 200:
        data = json.loads(res.text)
        info_about_weather = weather_another_city_detection(data, city)
        bot.send_message(message.chat.id, info_about_weather[0])
        bot.send_message(message.chat.id, info_about_weather[1])
        photo = get_photo_dog()
        bot.send_photo(message.chat.id, photo)

        bot.send_message(message.chat.id, 'Хотите узнать погоду в другом городе?',
                         reply_markup=yes_no_keyboard_inline())
    else:
        bot.send_message(message.chat.id, 'Город указан не верно')


@bot.callback_query_handler(func=lambda call: call.data == 'да')
def get_weather_again(call):
    message = call.message
    bot.send_message(message.chat.id, 'Снова введите город где вы хотите узнать погоду')


@bot.callback_query_handler(func=lambda call: call.data == 'нет')
def restart(call):
    message = call.message
    bot.delete_state(message.chat.id)
    bot.send_message(message.chat.id, 'Всего доброго:)\n'
                                      'Если хотите снова узнать погоду и поднять настроение, '
                                      'запустите бота снова через меню')
