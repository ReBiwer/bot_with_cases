from telebot.types import Message
from loader import bot
from database.logging import User
from datetime import datetime


@bot.message_handler(commands=["start"])
def bot_start(message: Message):
    user = User(username=message.from_user.username,
                action='/start',
                time_action=datetime.now(),
                )
    user.save()
    bot.send_message(message.chat.id, 'Приветствую, рад вас видеть! '
                                      'Выберите нужную команду в меню')
