from telebot.types import Message

from loader import bot


@bot.message_handler(commands=["start"])
def bot_start(message: Message):
    bot.send_message(message.chat.id, 'Приветствую, рад вас видеть! '
                                      'Напишите название города в котором вы хотите узнать погоду!')
