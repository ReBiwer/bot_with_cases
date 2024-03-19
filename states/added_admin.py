from telebot.handler_backends import State, StatesGroup


class GettingAdmin(StatesGroup):
    id_admin = int()
    username_admin = str()
