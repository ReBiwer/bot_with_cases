import requests
import json
from config_data.config import *


def get_name_now_city() -> str:
    req = requests.get(f'https://geo.ipify.org/api/v2/country,city?apiKey={API_KEY_get_ip}')
    if req.status_code == 200:
        data = json.loads(req.text)
        return data["location"]["city"]
    else:
        return 'Не удалось получить имя вашего текущего города'
