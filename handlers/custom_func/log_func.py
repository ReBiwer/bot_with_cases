from database.logging_users import UserAction
from database.logging_admins import AdminAction
from datetime import datetime
from telebot.types import Message
from .check_admin import check_admin_status


def log_action(action, message: Message, check_admin=False):
    if check_admin:
        admin_action = AdminAction(id_admin=message.from_user.id,
                                   usernam_admin=message.from_user.username,
                                   action=action,
                                   time_action=datetime.now(),
                                   )
        admin_action.save()
    else:
        user_action = UserAction(id_user=message.from_user.id,
                                 username=message.from_user.username,
                                 action=action,
                                 time_action=datetime.now(),
                                 )
        user_action.save()
