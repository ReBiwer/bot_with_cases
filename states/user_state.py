from telebot.handler_backends import State, StatesGroup


class UserState(StatesGroup):
    admin = False
    id = int()
    username = str()
    action = StatesGroup()
    current_message = None
