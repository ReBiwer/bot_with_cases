from telebot.types import Message

from handlers.custom_func.decorators import update_UserState_action
from loader import bot
from keyboards.inline.project_selection_keyboard import project_selection_keyboard
from states.user_state import UserState


@bot.message_handler(content_types=['text'])
@update_UserState_action
def bot_echo(message: Message):
    UserState.current_logger.info('content_types=["text"]')
    bot.send_message(message.chat.id, 'Вам сейчас не нужно вводить текст. Выберите команду',
                     reply_markup=project_selection_keyboard())
