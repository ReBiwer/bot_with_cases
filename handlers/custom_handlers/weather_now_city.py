from telebot.types import CallbackQuery
import requests
import json
from config_data.config import *
from loader import bot
from handlers.custom_func import *
from states.getting_weather import GettingWeather


@bot.callback_query_handler(func=lambda call: call.data == 'now_city')
def weather_now_city(call: CallbackQuery):
    message = call.message
    '''Получение текущего города пользователя и вывод погоды в его городе'''
    now_city = get_name_now_city() # получаем имя города пользователя
    if now_city != 'Не удалось получить имя вашего текущего города':
        data_about_weather = get_weather_city(now_city) # получаем информацию о погоде в городе
        if data_about_weather != 'Не удалось получить информацию о погоде в городе':
            info_about_weather = weather_now_city_detection(data_about_weather) # обрабатываем информацию о погоде в городе
            bot.send_message(message.chat.id, info_about_weather[0])
            bot.send_message(message.chat.id, info_about_weather[1])

            if isinstance(GettingWeather.downloads, str):
                bot.send_message(message.chat.id, GettingWeather.downloads)
            else:
                bot.send_photo(message.chat.id, GettingWeather.downloads)
        else:
            bot.send_message(message.chat.id, data_about_weather)
    else:
        bot.send_message(message.chat.id, now_city)