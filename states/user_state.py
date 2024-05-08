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
    password_for_decryption_file = str()
    path_to_file_for_encryption = State()
    path_to_file_for_decryption = State()
    extension_decrypt_file = str
    current_message: Message = None
    current_logger: Logger = None
    debug_logger: Logger = None
