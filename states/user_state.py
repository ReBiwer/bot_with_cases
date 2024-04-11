from telebot.handler_backends import State, StatesGroup


class UserState(StatesGroup):
    id = int()
    username = str()
    action = State()
