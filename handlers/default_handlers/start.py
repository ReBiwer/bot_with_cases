from telebot.types import Message

from keyboards.admin_buttons.inline.action_admin import action_admin
from loader import bot
from handlers.custom_func.log_func import log_action
from handlers.custom_func.check_admin import check_admin_status
from keyboards.inline.project_selection_keyboard import project_selection_keyboard
from states.getting_weather import GettingWeather
from handlers.custom_func.photo_dog import get_photo_dog


@bot.message_handler(commands=["start"])
def bot_start(message: Message):
    chat_id = message.chat.id
    if check_admin_status(message):
        log_action('commands = ["start"]', message, check_admin=True)

        bot.send_message(chat_id,
                         f'Приветствую вас, администратор {message.from_user.username}',
                         reply_markup=action_admin())
    else:
        bot.send_message(chat_id, 'Я бот Быкова Владимира\n'
                                  'Я создан с целью продемонстрировать кейсы моего создателя\n'
                                  'Если возникнут какие-то ошибки в работе бота, прошу сообщить об этом\n'
                                  'Кнопка репорта находится в "меню"')
        bot.send_message(chat_id, 'Выберите кейс, который вы бы хотели протестировать?',
                         reply_markup=project_selection_keyboard())
        log_action('commands = ["start"]', message)
        bot.send_message(chat_id, message)
