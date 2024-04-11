from telebot import TeleBot

from database.list_admins import Admins
from database.logging_users import UserAction
from database.logging_admins import AdminAction
from datetime import datetime
from telebot.types import Message, CallbackQuery


def log_action(action, message: Message | CallbackQuery, check_admin=False):
    if check_admin:
        if isinstance(message, Message):
            admin_action = AdminAction.create(id_admin=message.from_user.id,
                                              username_admin=message.from_user.username,
                                              action_admin=action,
                                              time_action=datetime.now(),
                                              )
            admin_action.save()
        elif isinstance(message, CallbackQuery):
            admin_action = AdminAction.create(id_admin=message.message.chat.id,
                                              username_admin=message.message.chat.username,
                                              action_admin=action,
                                              time_action=datetime.now(),
                                              )
            admin_action.save()
    else:
        if isinstance(message, Message):
            user_action = UserAction.create(id_user=message.from_user.id,
                                            username=message.from_user.username,
                                            action=action,
                                            time_action=datetime.now(),
                                            )
            user_action.save()
        elif isinstance(message, CallbackQuery):
            user_action = UserAction.create(id_user=message.message.chat.id,
                                            username=message.message.chat.username,
                                            action=action,
                                            time_action=datetime.now(),
                                            )
            user_action.save()


def put_log_info(bot: TeleBot, message: Message, check_admin=False):
    if check_admin:
        pass
    else:
        id_user = message.from_user.id
        username = message.from_user.username
        user_report = message.text
        actions_user = ''
        for user in UserAction.select().where(UserAction.id_user == id_user):
            actions_user += (f'ID_user: {user.id_user} -- '
                             f'username: {user.username} -- '
                             f'action: {user.action} -- '
                             f'time_action: {user.time_action}\n')
        id_admins = [admin.id_admin for admin in Admins.select()]
        with open(f'handlers/custom_func/logs/{id_user}_logfile.log', 'w') as log_file:
            log_file.write(str(actions_user))
        with open(f'handlers/custom_func/logs/{id_user}_logfile.log', 'r') as log_file:
            for id_chat in id_admins:
                bot.send_message(id_chat, 'Пришел новый репорт')
                bot.send_message(id_chat, f'Пользователь: {username}\n'
                                          f'id пользователя: {id_user}\n'
                                          f'Сообщение: {user_report}')
                bot.send_document(id_chat, log_file)
