import requests
import json
from config_data.config import *
from handlers.custom_func.decorators import update_UserState_action
from states.user_state import UserState


@update_UserState_action
def get_weather(city):
    req = requests.get(
        f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY_weather}&units=metric&lang=ru')
    if req.status_code == 200:
        data = json.loads(req.text)
        UserState.current_logger.info(f'Запрос погоды в городе {city} прошел успешно')
        return data
    else:
        UserState.current_logger.info(f'Запрос погоды в городе {city} прошел не успешно. '
                                      f'Статус кода: {req.status_code}')
        return 'Не удалось получить информацию о погоде в городе'
