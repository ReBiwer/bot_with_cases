from telebot.types import Message, CallbackQuery
import requests
import json
from config_data.config import *
from loader import bot
from states.getting_weather import GettingWeather
from keyboards.inline.yes_no_inline import yes_no_keyboard_inline
from handlers.custom_func import *


@bot.callback_query_handler(func=lambda call: call.data == 'another_city')
def weather_another_city(call: CallbackQuery):
    message = call.message
    bot.set_state(GettingWeather.id_user, GettingWeather.another_city)
    bot.send_message(message.chat.id, 'Введите город где вы хотите узнать погоду')


@bot.message_handler(state=GettingWeather.another_city)
def put_weather(message: Message):
    city = message.text.strip().lower()
    data_about_weather = get_weather_city(city)
    if data_about_weather != 'Не удалось получить информацию о погоде в городе':
        info_about_weather = weather_another_city_detection(data_about_weather, city)
        bot.send_message(message.chat.id, info_about_weather[0])
        bot.send_message(message.chat.id, info_about_weather[1])

        if isinstance(GettingWeather.downloads, str):
            bot.send_message(message.chat.id, GettingWeather.downloads)
        else:
            bot.send_photo(message.chat.id, GettingWeather.downloads)

        bot.send_message(message.chat.id, 'Хотите узнать погоду в другом городе?',
                         reply_markup=yes_no_keyboard_inline())
    else:
        bot.send_message(message.chat.id, data_about_weather)


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
