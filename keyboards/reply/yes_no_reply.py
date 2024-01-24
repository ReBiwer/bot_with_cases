from telebot.types import ReplyKeyboardMarkup, KeyboardButton

def yes_no_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(True, True)
    but_1 = KeyboardButton('Да')
    but_2 = KeyboardButton('Нет')
    keyboard.add(but_1, but_2)
    return keyboard
