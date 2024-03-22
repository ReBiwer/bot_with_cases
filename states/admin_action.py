from telebot.handler_backends import State, StatesGroup


class AdminAction(StatesGroup):
    name_admin = str()
    action = str()
