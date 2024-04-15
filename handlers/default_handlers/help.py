from telebot.types import Message

from handlers.custom_func.decorators import update_UserState_action
from handlers.custom_func.log_func import log_action
from loader import bot
from keyboards.inline.project_selection_keyboard import project_selection_keyboard
from handlers.project_weather.funcs.photo_dog import get_photo_dog
from states.user_state import UserState


@bot.message_handler(commands=["help"])
@update_UserState_action
def bot_help(message: Message):
    log_action('commands=["help"]', message)
    UserState.id = message.from_user.id
    UserState.username_user = message.from_user.username
    UserState.downloads = get_photo_dog(message)
    bot.send_message(message.chat.id, 'Этот бот предназанчен для получения погоды\n'
                                      'В вашем городе или в любом другом, в каком только захотите')
    bot.send_message(message.chat.id, 'Выберите где вы хотите узнать погоду', reply_markup=project_selection_keyboard())
