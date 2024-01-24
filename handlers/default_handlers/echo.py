from telebot.types import Message
import requests
from config_data.config import *
import json
from loader import bot


# Эхо хендлер, куда летят текстовые сообщения без указанного состояния
@bot.message_handler(content_types=['text'])
def bot_echo(message: Message):
    bot.send_message(message.chat.id, message.text)
