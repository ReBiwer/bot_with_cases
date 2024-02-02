from telebot.types import CallbackQuery
import requests
import json
from config_data.config import *
from loader import bot
from handlers.custom_func.weather_detection import weather_now_city_detection
from handlers.custom_func.get_photo_dog import get_photo_dog


@bot.callback_query_handler(func=lambda call: call.data == 'now_city')
def weather_now_city(call: CallbackQuery):
    message = call.message
    '''Получение текущего города пользователя и вывод погоды в его городе'''
    res_now_city = requests.get(f'https://geo.ipify.org/api/v2/country,city?apiKey={API_KEY_get_ip}')
    if res_now_city.status_code == 200:
        data_for_city = json.loads(res_now_city.text)
        now_city = data_for_city["location"]["city"]

        res_weather_city = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?q={now_city}&appid={API_KEY_weather}&units=metric&lang=ru')
        if res_weather_city.status_code == 200:
            data_for_weather = json.loads(res_weather_city.text)
            info_for_weather = weather_now_city_detection(data_for_weather)
            bot.send_message(message.chat.id, info_for_weather)
            photo = get_photo_dog()
            bot.send_photo(message.chat.id, photo)
        else:
            bot.send_message(message.chat.id, 'Не можем получить информацию о погоде(\n'
                                              'Сервер не хочет говорить..')
    else:
        bot.send_message(message.chat.id, 'Проблема с тем, чтобы узнать ваш город(\n'
                                          'Сервер не хочет говорить..')
