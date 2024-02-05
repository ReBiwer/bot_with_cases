from telebot.types import Message
from loader import bot
from database.logging import User
from datetime import datetime
from keyboards.inline.select_city import keyboard_selecе_city
from states.getting_weather import GettingWeather
from handlers.custom_func.photo_dog import get_photo_dog


@bot.message_handler(commands=["start"])
def bot_start(message: Message):
    user = User(id_user=message.from_user.id,
                username=message.from_user.username,
                action='/start',
                time_action=datetime.now(),
                )
    user.save()
    bot.set_state(message.from_user.id, GettingWeather.id_user, message.chat.id)
    GettingWeather.username_user = message.from_user.username
    GettingWeather.downloads = get_photo_dog()
    GettingWeather.id_user = message.from_user.id
    bot.send_message(message.chat.id, 'Приветствую, рад вас видеть!')
    bot.send_message(message.chat.id, 'В каком городе вы хотите узнать погоду?', reply_markup=keyboard_selecе_city())

