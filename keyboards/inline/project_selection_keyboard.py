from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup


def project_selection_keyboard() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(row_width=1)
    but_1 = InlineKeyboardButton('Узнать погоду в своем городе', callback_data='weather_user_city')
    # but_2 = InlineKeyboardButton('В другом городе', callback_data='another_city')
    keyboard.add(but_1)
    return keyboard
