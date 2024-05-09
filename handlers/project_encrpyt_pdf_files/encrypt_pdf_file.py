from PyPDF2 import PdfFileWriter, PdfFileReader
from telebot.types import CallbackQuery, Message
from states.user_state import UserState
from loader import bot
from handlers.custom_func.decorators import update_UserState_action


@bot.callback_query_handler(func=lambda call: call.data == 'encrypt_pdf_file')
@update_UserState_action
def request_pdf_file(call: CallbackQuery):
    """Запрос PDF файла для шифрования"""
    pass


@update_UserState_action
def get_pdf_file(message: Message):
    """Получение файла PDF, создание класса PdfFileWriter, запрос пароля для шифрования"""
    pass


@update_UserState_action
def send_encrypt_pdf_file(message: Message):
    """Получения пароля для шифрования, шифрование файла, отправка файла пользователю"""
    pass
