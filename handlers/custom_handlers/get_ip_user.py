from telebot.types import Message
import requests
import json
from config_data.config import *
from loader import bot


@bot.message_handler(commands=["get_ip_user"])
def get_user_ip(message: Message):
    res = requests.get(f'https://geo.ipify.org/api/v2/country,city?apiKey={API_KEY_get_ip}')
    if res.status_code == 200:
        data = json.loads(res.text)
        user_ip = data["ip"]
        user_loc = data["location"]
        exact_loc_user = (f'Страна: {user_loc["country"]}\n'
                          f'Регион: {user_loc["region"]}\n'
                          f'Город: {user_loc["city"]}')
        bot.send_message(message.chat.id, f'Ваш IP: {user_ip}')
        bot.send_message(message.chat.id, f'Ваше местоположение:\n{exact_loc_user}')
    else:
        bot.send_message(message.chat.id, 'Проблема с сервером(')
