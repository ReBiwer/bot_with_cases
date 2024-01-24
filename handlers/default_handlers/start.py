from telebot.types import Message
from states.getting_weather import GettingWeather
from loader import bot


@bot.message_handler(commands=["start"])
def bot_start(message: Message):
    bot.send_message(message.chat.id, 'Приветствую, рад вас видеть! '
                                      'Выберите нужную команду в меню')
