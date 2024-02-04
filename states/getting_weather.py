from telebot.handler_backends import State, StatesGroup


class GettingWeather(StatesGroup):
    id_user = State()
    username_user = State()
    another_city = State()
    now_city = State()
    restart = State()
    downloads = State()
