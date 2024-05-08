from logging import Logger
from telebot.types import Message, CallbackQuery
from handlers.custom_func.decorators import update_UserState_action
from states.user_state import UserState
from keyboards.admin_keyboards.inline.action_admin import action_admin
from loader import bot
from handlers.custom_func.log_func import get_logger
from handlers.custom_func.check_admin import check_admin_status
from keyboards.inline.project_selection_keyboard import project_selection_keyboard
from keyboards.admin_keyboards.inline.user_choice import user_choice


@bot.message_handler(commands=["start"])
@update_UserState_action
def bot_start(message: Message):
    name_user = message.chat.username if message.chat.username else message.chat.first_name
    id_user = message.chat.id
    logger, debug_logger = get_logger(name_user, id_user)

    UserState.current_logger = logger
    UserState.debug_logger = debug_logger
    UserState.username = name_user
    chat_id = message.chat.id
    UserState.admin_status = check_admin_status(message)
    if UserState.admin_status:
        UserState.current_logger.info('Команда - start')
        bot.send_message(chat_id,
                         f'Приветствую вас, администратор {message.chat.username}\n'
                         f'Как бы вы хотели продолжить?',
                         reply_markup=user_choice())
    else:
        bot.send_message(chat_id, 'Я бот Быкова Владимира\n'
                                  'Я создан с целью продемонстрировать кейсы моего создателя\n'
                                  'Если возникнут какие-то ошибки в работе бота, прошу сообщить об этом\n'
                                  'Кнопка репорта находится в "меню"')
        bot.send_message(chat_id, 'Выберите кейс, который вы бы хотели протестировать?',
                         reply_markup=project_selection_keyboard())
        UserState.current_logger.info('Команда - start')


@bot.callback_query_handler(func=lambda call: call.data == 'admin_direction')
@update_UserState_action
def start_admin(call: CallbackQuery):
    chat_id = call.message.chat.id
    UserState.admin_access = True
    bot.send_message(chat_id, f'Приветствую вас, администратор {call.message.chat.username}\n'
                              f'Что хотите протестировать?', reply_markup=action_admin())


@bot.callback_query_handler(func=lambda call: call.data == 'user_direction')
@update_UserState_action
def start_user(call: CallbackQuery):
    chat_id = call.message.chat.id
    UserState.admin_access = False
    bot.send_message(chat_id, 'Я бот Быкова Владимира\n'
                              'Я создан с целью продемонстрировать кейсы моего создателя\n'
                              'Если возникнут какие-то ошибки в работе бота, прошу сообщить об этом\n'
                              'Кнопка репорта находится в "меню"')
    bot.send_message(chat_id, 'Выберите кейс, который вы бы хотели протестировать?',
                     reply_markup=project_selection_keyboard())
    UserState.current_logger.info(f'Администратор {call.message.chat.username} зашел как пользователь')


@bot.callback_query_handler(func=lambda call: call.data == 'restart')
@update_UserState_action
def restart(call: CallbackQuery):
    message = call.message
    chat_id = message.chat.id
    UserState.current_logger.info('команда - рестарт')
    if UserState.admin_status:
        bot.send_message(chat_id,
                         f'Снова приветствую вас, администратор {message.chat.username}\n'
                         f'Как бы вы хотели продолжить?',
                         reply_markup=user_choice())
    else:
        bot.send_message(chat_id, 'Я бот Быкова Владимира\n'
                                  'Я создан с целью продемонстрировать кейсы моего создателя\n'
                                  'Если возникнут какие-то ошибки в работе бота, прошу сообщить об этом\n'
                                  'Кнопка репорта находится в "меню"')
        bot.send_message(chat_id, 'Выберите кейс, который вы бы хотели протестировать?',
                         reply_markup=project_selection_keyboard())
