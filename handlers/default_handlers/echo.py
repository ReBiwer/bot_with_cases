from telebot.types import Message

from handlers.custom_func.decorators import update_UserState_action
from loader import bot
from handlers.custom_func.log_func import log_action
from keyboards.inline.project_selection_keyboard import project_selection_keyboard


@bot.message_handler(content_types=['text'])
@update_UserState_action
def bot_echo(message: Message):
    log_action('content_types=["text"]', message)
    bot.send_message(message.chat.id, 'Вам сейчас не нужно вводить текст. Выберите команду',
                     reply_markup=project_selection_keyboard())
