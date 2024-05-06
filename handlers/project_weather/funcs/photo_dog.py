import json
import requests
from handlers.custom_func.decorators import update_UserState_action
from telebot.types import Message
from states.user_state import UserState


@update_UserState_action
def get_photo_dog():
    req_url_photo = requests.get('https://dog.ceo/api/breeds/image/random')
    if req_url_photo.status_code == 200:
        data_req_url_photo = json.loads(req_url_photo.text)
        url_photo = data_req_url_photo['message']
        req_photo = requests.get(url_photo).content
        UserState.current_logger.info(f'Запрос фотографии прошел успешно')
        return req_photo
    else:
        UserState.current_logger.info(f'Запрос фотографии прошел не успешно. Статус кода: {req_url_photo.status_code}')
        return 'Не удалось получить фото с песиком('
