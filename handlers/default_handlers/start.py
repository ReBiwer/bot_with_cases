from telebot.types import Message
from loader import bot
from database.logging import User
from datetime import datetime
from keyboards.inline.select_city import keyboard_selecе_city
from states.getting_weather import GettingWeather
import requests
import json


@bot.message_handler(commands=["start"])
def bot_start(message: Message):
    load_photo()
    user = User(id_user=message.from_user.id,
                username=message.from_user.username,
                action='/start',
                time_action=datetime.now(),
                )
    user.save()
    bot.set_state(message.from_user.id, GettingWeather.id_user, message.chat.id)
    GettingWeather.id_user = message.from_user.id
    bot.send_message(message.chat.id, 'Приветствую, рад вас видеть!')
    bot.send_message(message.chat.id, 'В каком городе вы хотите узнать погоду?', reply_markup=keyboard_selecе_city())


def load_photo():
    req_url_photo = requests.get('https://dog.ceo/api/breeds/image/random')
    data_req_url_photo = json.loads(req_url_photo.text)
    url_photo = data_req_url_photo['message']
    req_photo = requests.get(url_photo).content
    with open('images/dog_image.jpg', 'wb') as photo:
        photo.write(req_photo)
