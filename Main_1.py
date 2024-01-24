from telebot import *
import requests
import json

bot = TeleBot('6845585691:AAHvWslzRvwxq9LEzhdX7vKo1vEpkwPN35w')
API = '44fb8db4a710c0322de424c1a66779b7'


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Приветствую, рад вас видеть! '
                                      'Напишите название города в котором вы хотите узнать погоду!')


@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    if res.status_code == 200:
        data = json.loads(res.text)
        temp_in_city = data["main"]["temp"]
        bot.reply_to(message, f'Погода в городе {city.capitalize()}: {temp_in_city}')
        image = 'sunny_weather.jpg' if temp_in_city < 5.0 else 'sun_weather.jpg'
        with open('images/' + image, 'rb') as file:
            bot.send_photo(message.chat.id, file)
    else:
        bot.send_message(message.chat.id, 'Город указан не верно')


bot.polling(non_stop=True)
