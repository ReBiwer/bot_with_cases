from telebot.types import Message
import requests
from config_data.config import *
import json
from loader import bot
from handlers.custom_func.log_func import log_action
from keyboards.inline.select_city import keyboard_selecе_city


@bot.message_handler(content_types=['text'])
def bot_echo(message: Message):
    log_action('content_types=["text"]')
    bot.send_message(message.chat.id, 'Вам сейчас не нужно вводить текст. Выберите команду',
                     reply_markup=keyboard_selecе_city())
