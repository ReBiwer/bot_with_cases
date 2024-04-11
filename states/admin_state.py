from telebot.handler_backends import State, StatesGroup


class AdminState(StatesGroup):
    id = int()
    username = str()
    action = State()
