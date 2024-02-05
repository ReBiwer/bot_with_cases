from telebot.handler_backends import State, StatesGroup


class GettingWeather(StatesGroup):
    id_user = int()
    username_user = str()
    downloads = State()
    city_username = State()
    another_city = State()
