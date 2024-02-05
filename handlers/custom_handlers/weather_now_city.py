from telebot.types import CallbackQuery
import requests
import json
from config_data.config import *
from loader import bot
from handlers.custom_func.name_now_city import get_name_now_city
from handlers.custom_func.weather_detection import weather_detection
from handlers.custom_func.weather_in_city import get_weather
from states.getting_weather import GettingWeather
from handlers.custom_func.log_func import log_action


@bot.callback_query_handler(func=lambda call: call.data == 'city_username')
def weather_now_city(call: CallbackQuery):
    '''Получение текущего города пользователя и вывод погоды в его городе'''
    message = call.message
    log_action('call.data = "city_username"')
    city_username = get_name_now_city() # получаем имя города пользователя
    if city_username != 'Не удалось получить имя вашего текущего города':
        data_about_weather = get_weather(city_username) # получаем информацию о погоде в городе
        if data_about_weather != 'Не удалось получить информацию о погоде в городе':
            info_about_weather = weather_detection(data_about_weather) # обрабатываем информацию о погоде в городе
            bot.send_message(message.chat.id, info_about_weather[0])
            bot.send_message(message.chat.id, info_about_weather[1])

            if isinstance(GettingWeather.downloads, str):
                bot.send_message(message.chat.id, GettingWeather.downloads)
            else:
                bot.send_photo(message.chat.id, GettingWeather.downloads)
        else:
            bot.send_message(message.chat.id, data_about_weather)
    else:
        bot.send_message(message.chat.id, city_username)