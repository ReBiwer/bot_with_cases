from database.list_admins import Admin
from loader import bot
from telebot.types import Message


@bot.message_handler(commands=['add_admin'])
def add_admin(message: Message):
    all_admins = [admin.id_admin for admin in Admin.select()]
    if message.from_user.id not in all_admins:
        new_admin = Admin(id_admin=message.from_user.id,
                          username_admin=message.from_user.username)
        new_admin.save()
        bot.send_message(message.chat.id, f'Добавлен новый администратор:\n'
                                          f'id: {Admin.id_admin}\n'
                                          f'username: {Admin.username_admin}')
    else:
        bot.send_message(message.chat.id, f'Пользователь {message.from_user.username} '
                                          f'уже является администратором этого бота')
