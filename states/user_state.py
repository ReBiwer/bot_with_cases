from telebot.handler_backends import State, StatesGroup


class UserState(StatesGroup):
    admin = False
    id = int()
    username = str()
    action = str()
    downloads = State()
    city_username = State()
    current_message = None
