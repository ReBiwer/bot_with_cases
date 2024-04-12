from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup


def restart_keyboard() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup()
    but = InlineKeyboardButton('Вернуться в меню', callback_data='restart')
    keyboard.add(but)
    return keyboard
