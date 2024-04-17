from telebot import TeleBot
import os
from database.list_admins import Admins
from database.logging_users import UserAction
from database.logging_admins import AdminAction
from datetime import datetime
from telebot.types import Message, CallbackQuery

from states.user_state import UserState


def log_action(mess_log, message: Message | CallbackQuery):
    if UserState.admin_access:
        admin_action = AdminAction.create(id_admin=message.chat.id,
                                          username_admin=message.chat.username,
                                          action_admin=f'handler: {UserState.action} -- '
                                                       f'message: {mess_log} -- '
                                                       f'access right: admin',
                                          time_action=datetime.now(),
                                          )
        admin_action.save()
    else:
        user_action = UserAction.create(id_user=message.chat.id,
                                        username=message.chat.username,
                                        action=f'handler: {UserState.action} -- '
                                               f'message: {mess_log} -- '
                                               f'access right: user',
                                        time_action=datetime.now(),
                                        )
        user_action.save()


def put_log_info(bot: TeleBot, message: Message):
    if UserState.admin_access:
        pass
    else:
        current_date = datetime.now()
        format_date = '%Y-%m-%d %H:%M:%S'
        day_ago: str = (f'{current_date.year}-{current_date.month}-{current_date.day-1} '
                        f'{current_date.hour}:{current_date.minute}:{current_date.second}')
        date_day_ago = datetime.strptime(day_ago, format_date)
        id_user = message.chat.id
        username = message.chat.username
        user_report = message.text
        actions_user = ''
        for user in UserAction.select().where(UserAction.id_user == id_user and UserAction.time_action > date_day_ago):
            actions_user += (f'ID_user: {user.id_user} -- '
                             f'username: {user.username} -- '
                             f'action: {user.action} -- '
                             f'time_action: {user.time_action}\n')
        id_admins = [admin.id_admin for admin in Admins.select()]
        if not os.path.exists('handlers/custom_func/logs'):
            os.mkdir('handlers/custom_func/logs')
        with open(f'handlers/custom_func/logs/{id_user}_logfile.log', 'w', encoding='utf-8') as log_file:
            log_file.write(actions_user)
        with open(f'handlers/custom_func/logs/{id_user}_logfile.log', 'r', encoding='utf-8') as log_file:
            for id_chat in id_admins:
                bot.send_message(id_chat, 'Пришел новый репорт')
                bot.send_message(id_chat, f'Пользователь: {username}\n'
                                          f'id пользователя: {id_user}\n'
                                          f'Сообщение: {user_report}')
                bot.send_document(id_chat, log_file)
