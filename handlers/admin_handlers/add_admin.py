from database.list_admins import Admins
from handlers.custom_func.decorators import update_UserState_action
from handlers.custom_func.log_func import log_action
from loader import bot
from telebot.types import Message


@bot.message_handler(commands=['add_admin'])
@update_UserState_action
def add_admin(message: Message):
    id_all_admins = [admin.id_admin for admin in Admins.select()]
    name_admin = message.chat.username if message.chat.username else message.chat.first_name
    if message.from_user.id not in id_all_admins:
        new_admin = Admins(id_admin=message.from_user.id,
                           username_admin=name_admin,)
        bot.send_message(message.chat.id, f'Добавлен новый администратор:\n'
                                          f'id: {new_admin.id_admin}\n'
                                          f'name: {new_admin.username_admin}')
        new_admin.save()
        log_action(f'Команда - add_admin, new_admin - {new_admin.username_admin}', message)
    else:
        bot.send_message(message.chat.id, f'Пользователь {name_admin} '
                                          f'уже является администратором этого бота')
        log_action(f'Команда - add_admin, администратор {name_admin} уже есть', message)
