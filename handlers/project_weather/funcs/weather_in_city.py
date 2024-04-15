import requests
import json
from config_data.config import *
from handlers.custom_func.decorators import update_UserState_action
from handlers.custom_func.log_func import log_action
from telebot.types import Message
from loader import bot
from states.user_state import UserState


@update_UserState_action
def get_weather(city, message: Message):
    req = requests.get(
        f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY_weather}&units=metric&lang=ru')
    if req.status_code == 200:
        data = json.loads(req.text)
        log_action(f'Запрос погоды в городе {city} прошел успешно', message)
        return data
    else:
        log_action(f'Запрос погоды в городе {city} прошел не успешно. Статус кода: {req.status_code}', message)
        return 'Не удалось получить информацию о погоде в городе'
