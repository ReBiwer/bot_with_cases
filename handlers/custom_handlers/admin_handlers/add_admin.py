from database.list_admins import Admins
from loader import bot
from telebot.types import Message


@bot.message_handler(commands=['add_admin'])
def add_admin(message: Message):
    id_all_admins = [admin.id_admin for admin in Admins.select()]
    if message.from_user.id not in id_all_admins:
        new_admin = Admins(id_admin=message.from_user.id,
                           username_admin=message.from_user.username)
        new_admin.save()
        bot.send_message(message.chat.id, f'Добавлен новый администратор:\n'
                                          f'id: {Admins.id_admin}\n'
                                          f'username: {Admins.username_admin}')
    else:
        bot.send_message(message.chat.id, f'Пользователь {message.from_user.username} '
                                          f'уже является администратором этого бота')
