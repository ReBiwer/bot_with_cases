from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup


def action_admin() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(row_width=1)
    but_1 = InlineKeyboardButton('Узнать погоду в другом городе (через API)', callback_data='another_city')
    keyboard.add(but_1)
    return keyboard
