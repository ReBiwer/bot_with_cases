from telebot.handler_backends import State, StatesGroup


class GettingWeather(StatesGroup):
    id_user = State()
    city = State()
