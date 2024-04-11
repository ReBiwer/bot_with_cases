import requests
import json
from config_data.config import *
from handlers.custom_func.log_func import log_action
from telebot.types import Message
from loader import bot
from states.user_state import UserState


def get_name_now_city(message: Message) -> str:
    req = requests.get(f'https://geo.ipify.org/api/v2/country,city?apiKey={API_KEY_get_ip}')
    current_state: UserState = bot.get_state(message.chat.id)
    name_cur_state: str = current_state.__name__
    name_cur_action: str = current_state.action.__name__
    if req.status_code == 200:
        data = json.loads(req.text)
        city = data["location"]["city"]
        log_action(f'state={name_cur_state}, action={name_cur_action}\n'
                   f'Статус запроса: {req.status_code}, имя города получено: {city} ', message)
        return city
    else:
        log_action(f'state={name_cur_state}, action={name_cur_action}\n'
                   f'Статус запроса: {req.status_code}, ошибка: {req.text}', message)
        return 'Не удалось получить имя вашего текущего города'
