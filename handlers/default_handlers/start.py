from telebot.types import Message
from states.getting_weather import GettingWeather
from loader import bot


@bot.message_handler(commands=["start"])
def bot_start(message: Message):
    bot.set_state(message.from_user.id, GettingWeather.city, message.chat.id)
    bot.send_message(message.chat.id, 'Приветствую, рад вас видеть! '
                                      'Напишите название города в котором вы хотите узнать погоду!')
