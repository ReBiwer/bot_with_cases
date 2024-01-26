from telebot.handler_backends import State, StatesGroup


class GettingWeather(StatesGroup):
    city = State()
