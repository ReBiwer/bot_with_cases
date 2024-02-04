from telebot.handler_backends import State, StatesGroup


class GettingWeather(StatesGroup):
    id_user = State()
    username_user = State()
    city = State()
    downloads = State()
