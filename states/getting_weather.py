from telebot.handler_backends import State, StatesGroup


class GettingWeather(StatesGroup):
    downloads = State()
    city_username = State()
