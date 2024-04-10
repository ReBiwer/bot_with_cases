from telebot import TeleBot

from database.list_admins import Admins
from database.logging_users import UserAction
from database.logging_admins import AdminAction
from datetime import datetime
from telebot.types import Message


def log_action(action, message: Message, check_admin=False):
    if check_admin:
        admin_action = AdminAction.create(id_admin=message.from_user.id,
                                          username_admin=message.from_user.username,
                                          action_admin=action,
                                          time_action=datetime.now(),
                                          )
        admin_action.save()
    else:
        user_action = UserAction.create(id_user=message.from_user.id,
                                        username=message.from_user.username,
                                        action=action,
                                        time_action=datetime.now(),
                                        )
        user_action.save()


def get_log_info(bot: TeleBot, id_user, check_admin=False):
    if check_admin:
        pass
    else:
        actions_user = UserAction.select().where(UserAction.id_user == id_user)
        id_admins = [admin.id_admin for admin in Admins.select()]
        with open('handlers/custom_func/logs/test_logfile.log', 'w') as log_file:
            log_file.writelines(actions_user)
            for id_chat in id_admins:
                bot.send_message(id_chat, 'Пришел новый репорт')
                bot.send_document(id_chat, log_file)
