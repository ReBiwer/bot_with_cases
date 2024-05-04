from telebot.handler_backends import State, StatesGroup


class UserState(StatesGroup):
    admin_access = False
    admin_status = False
    id = int()
    username = str()
    action = str()
    downloads = State()
    city_username = State()
    current_message = None
    current_logger = None
