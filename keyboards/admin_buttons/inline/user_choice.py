from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup


def user_choice() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(row_width=2)
    but_user = InlineKeyboardButton('Как обычный пользователь', callback_data='user_direction')
    but_admin = InlineKeyboardButton('Как обычный пользователь', callback_data='admin_direction')
    keyboard.add(but_user, but_admin)
    return keyboard
