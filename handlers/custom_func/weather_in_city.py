import requests
import json
from config_data.config import *


def get_weather(city):
    req = requests.get(
        f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY_weather}&units=metric&lang=ru')
    if req.status_code == 200:
        data = json.loads(req.text)
        return data
    else:
        return 'Не удалось получить информацию о погоде в городе'
