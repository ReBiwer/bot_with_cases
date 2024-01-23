from telebot.types import Message
import requests
from config_data.config import *
import json
from loader import bot


# Эхо хендлер, куда летят текстовые сообщения без указанного состояния
@bot.message_handler(content_types=['text'])
def bot_echo(message: Message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={RAPID_API_KEY}&units=metric')
    if res.status_code == 200:
        data = json.loads(res.text)
        temp_in_city = data["main"]["temp"]
        bot.reply_to(message, f'Погода в городе {city.capitalize()}: {temp_in_city}')
        image = 'sunny_weather.jpg' if temp_in_city < 5.0 else 'sun_weather.jpg'
        with open('images/' + image, 'rb') as file:
            bot.send_photo(message.chat.id, file)
    else:
        bot.send_message(message.chat.id, 'Город указан не верно')
