import requests
import json
from config_data.config import *
from handlers.custom_func.log_func import log_action
from telebot.types import Message
from loader import bot
from states.user_state import UserState


def get_weather(city, message: Message):
    req = requests.get(
        f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY_weather}&units=metric&lang=ru')
    name_cur_state: str = UserState.__name__
    name_cur_action: str = UserState.action
    if req.status_code == 200:
        data = json.loads(req.text)
        log_action(f'state={name_cur_state}, action={name_cur_action}\n'
                   f'Статус запроса: {req.status_code}, информация о погоде: {data}', message)
        return data
    else:
        log_action(f'state={name_cur_state}, action={name_cur_action}\n'
                   f'Статус запроса: {req.status_code}, информация о погоде: {req.text}', message)
        return 'Не удалось получить информацию о погоде в городе'
