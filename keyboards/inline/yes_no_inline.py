from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup


def keyboard_inline(callback_yes, callback_no) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup()
    but_1 = InlineKeyboardButton('Да', callback_data=callback_yes)
    but_2 = InlineKeyboardButton('Нет', callback_data=callback_no)
    keyboard.add(but_1, but_2)
    return keyboard
