from telebot.types import Message, CallbackQuery
from states.user_state import UserState
from keyboards.admin_keyboards.inline.action_admin import action_admin
from loader import bot
from handlers.custom_func.log_func import log_action
from handlers.custom_func.check_admin import check_admin_status
from keyboards.inline.project_selection_keyboard import project_selection_keyboard
from keyboards.admin_keyboards.inline.user_choice import user_choice


@bot.message_handler(commands=["start"])
def bot_start(message: Message):
    chat_id = message.chat.id
    bot.set_state(message.from_user.id, UserState, chat_id)
    if check_admin_status(message):
        log_action('Команда - start', message)

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
        log_action('Команда - start', message)


@bot.callback_query_handler(func=lambda call: call.data == 'admin_direction')
def start_admin(call: CallbackQuery):
    chat_id = call.message.chat.id
    UserState.admin = True
    bot.send_message(chat_id, f'Приветствую вас, администратор {call.message.chat.username}\n'
                              f'Что хотите протестировать?', reply_markup=action_admin())
    log_action(f'Администратор {call.message.chat.username} зашел как админ', call.message)


@bot.callback_query_handler(func=lambda call: call.data == 'user_direction')
def start_admin(call: CallbackQuery):
    chat_id = call.message.chat.id
    UserState.admin = False
    bot.send_message(chat_id, 'Я бот Быкова Владимира\n'
                              'Я создан с целью продемонстрировать кейсы моего создателя\n'
                              'Если возникнут какие-то ошибки в работе бота, прошу сообщить об этом\n'
                              'Кнопка репорта находится в "меню"')
    bot.send_message(chat_id, 'Выберите кейс, который вы бы хотели протестировать?',
                     reply_markup=project_selection_keyboard())
    log_action(f'Администратор {call.message.chat.username} зашел как пользователь', call.message)


@bot.callback_query_handler(func=lambda call: call.data == 'restart')
def restart(call: CallbackQuery):
    message = call.message
    chat_id = message.chat.id
    log_action('Команда - рестарт', message)
    if UserState.admin:
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
