import requests
import json
from config_data.config import *
from handlers.custom_func.decorators import update_UserState_action
from handlers.custom_func.log_func import log_action
from telebot.types import Message
from loader import bot
from states.user_state import UserState


@update_UserState_action
def get_name_now_city(message: Message) -> str:
    req = requests.get(f'https://geo.ipify.org/api/v2/country,city?apiKey={API_KEY_get_ip}')
    name_cur_state: str = UserState.__name__
    name_cur_action: str = UserState.action
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
