import requests
import json
from config_data.config import *
from handlers.custom_func.decorators import update_UserState_action
from telebot.types import Message
from states.user_state import UserState


@update_UserState_action
def get_name_now_city(message: Message) -> str:
    req = requests.get(f'https://geo.ipify.org/api/v2/country,city?apiKey={API_KEY_get_ip}')
    if req.status_code == 200:
        data = json.loads(req.text)
        city = data["location"]["city"]
        UserState.current_logger.info(f'Запрос города успешный')
        return city
    else:
        UserState.current_logger.info(f'Запрос города не успешный. Статус кода: {req.status_code}')
        return 'Не удалось получить имя вашего текущего города'
