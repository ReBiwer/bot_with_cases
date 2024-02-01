from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup


def yes_no_keyboard_inline() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup()
    but_1 = InlineKeyboardButton('Да', callback_data='да')
    but_2 = InlineKeyboardButton('Нет', callback_data='нет')
    keyboard.add(but_1, but_2)
    return keyboard
