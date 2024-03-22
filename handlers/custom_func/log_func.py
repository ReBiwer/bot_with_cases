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
