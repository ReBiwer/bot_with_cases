from database.list_admins import Admin
from telebot.types import Message


def check_admin_status(message: Message):
    id_all_admins = [admin.id_admin for admin in Admin.select()]
    id_user = message.from_user.id
    if id_user in id_all_admins:
        return True
    else:
        return False
