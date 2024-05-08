from logging import Logger
from telebot.handler_backends import State, StatesGroup
from telebot.types import Message


class UserState(StatesGroup):
    admin_access = False
    admin_status = False
    id = int()
    username = str()
    action = str()
    downloads = State()
    city_username = State()
    password_to_encryption_file = int()
    path_to_file_for_encryption = State()
    current_message: Message = None
    current_logger: Logger = None
    debug_logger: Logger = None
