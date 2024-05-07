import pyAesCrypt
from telebot.types import CallbackQuery, Message
from handlers.custom_func.decorators import update_UserState_action
from keyboards.inline.restart import restart_button
from loader import bot
from states.user_state import UserState


def request_file_for_encryption(message: Message):
    """Запрашиваем файл, который пользователь хочет зашифровать"""
    pass


def get_file_for_encryption(call: CallbackQuery):
    """Получаем файл, который нужно зашифровать и запрашиваем пароль для шифрования.
    P.S. написать пользователю, чтобы название файла не изменял"""
    pass


def send_encryption_file(call: CallbackQuery):
    """Получаем пароль для дешифровки файла и скидываем зашифрованный файл"""
    pass


def get_encryption_file(message: Message):
    """Получаем зашифрованный файл и запрашиваем пароль для дешифровки"""
    pass


def send_decryption_file(call: CallbackQuery):
    """Получаем пароль для дешифровки файла, дешифруем файл и отправляем пользователю"""
    pass
