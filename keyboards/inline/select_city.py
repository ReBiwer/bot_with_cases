from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup


def keyboard_selecе_city() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(row_width=1)
    but_1 = InlineKeyboardButton('В моем городе', callback_data='now_city')
    but_2 = InlineKeyboardButton('В другом городе', callback_data='another_city')
    keyboard.add(but_1, but_2)
    return keyboard
