import pyAesCrypt
from telebot.types import CallbackQuery, Message
from handlers.custom_func.decorators import update_UserState_action
from keyboards.inline.restart import restart_button
from loader import bot
from states.user_state import UserState


@bot.callback_query_handler(func=lambda call: call == "encrypt_file")
@update_UserState_action
def request_file_for_encryption(call: CallbackQuery):
    """Запрашиваем файл, который пользователь хочет зашифровать"""
    message = call.message
    UserState.current_logger.info('Запрос файла для шифрования')
    response = bot.send_message(message.chat.id, 'Загрузите файл формата txt, который вы хотите зашифровать')
    bot.register_next_step_handler(response, get_file_for_encryption)


@update_UserState_action
def get_file_for_encryption(message: Message):
    """Получаем файл, который нужно зашифровать и запрашиваем пароль для шифрования"""
    UserState.current_logger.info('Получение файла для шифрования. Запрос пароля')


@update_UserState_action
def send_encryption_file(message: Message):
    """Получаем пароль для дешифровки файла и скидываем зашифрованный файл.
    P.S. написать пользователю, чтобы название файла не изменял"""
    UserState.current_logger.info('Отправка зашифрованного файла')


@update_UserState_action
def request_encryption_file(call: CallbackQuery):
    """Получаем зашифрованный файл и запрашиваем пароль для дешифровки.
    P.S. написать пользователю, что имя файла должно быть таким же, какое было присвоено этим ботом"""
    UserState.current_logger.info('Запрос файла для дешифрования')


@update_UserState_action
def get_password_for_decryption(message: Message):
    """Получаем зашифрованный файл и запрашиваем пароль для дешифрования"""
    UserState.current_logger.info('Получение файла для дешифрования. Запрос пароля')


@update_UserState_action
def send_decryption_file(message: Message):
    """Получаем пароль для дешифровки файла, дешифруем файл и отправляем пользователю"""
    UserState.current_logger.info('Отправка дешифрованного файла')
