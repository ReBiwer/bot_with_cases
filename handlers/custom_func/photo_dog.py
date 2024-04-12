import json
import requests

from handlers.custom_func.decorators import update_UserState_action
from handlers.custom_func.log_func import log_action
from telebot.types import Message
from loader import bot
from states.user_state import UserState


@update_UserState_action
def get_photo_dog(message: Message):
    name_cur_state: str = UserState.__name__
    name_cur_action: str = UserState.action
    req_url_photo = requests.get('https://dog.ceo/api/breeds/image/random')
    if req_url_photo.status_code == 200:
        data_req_url_photo = json.loads(req_url_photo.text)
        url_photo = data_req_url_photo['message']
        req_photo = requests.get(url_photo).content
        log_action(f'state={name_cur_state}, action={name_cur_action}\n'
                   f'Статус запроса: {req_url_photo.status_code}, фотография была получена', message)
        return req_photo
    else:
        log_action(f'state={name_cur_state}, action={name_cur_action}\n'
                   f'Статус запроса: {req_url_photo.status_code}, ошибка: {req_url_photo.text}', message)
        return 'Не удалось получить фото с песиком('
