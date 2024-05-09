import os
from PyPDF2 import PdfFileWriter, PdfFileReader
from telebot.types import CallbackQuery, Message
from states.user_state import UserState
from loader import bot
from handlers.custom_func.decorators import update_UserState_action


@bot.callback_query_handler(func=lambda call: call.data == 'encrypt_pdf_file')
@update_UserState_action
def request_pdf_file(call: CallbackQuery):
    """Запрос PDF файла для шифрования"""
    message = call.message
    chat_id = message.chat.id
    response = bot.send_message(chat_id, 'Скиньте PDF файл, на который вы хотите поставить пароль')
    bot.register_next_step_handler(response, get_pdf_file)


@update_UserState_action
def get_pdf_file(message: Message):
    """Получение файла PDF, создание класса PdfFileWriter, запрос пароля для шифрования"""
    chat_id = message.chat.id

    path_file = bot.get_file(message.document.file_id).file_path
    UserState.unic_pdf_name, extension_file = get_name_extension(path_file)
    UserState.pdf_file_user = bot.download_file(path_file)
    response = bot.send_message(chat_id, 'Введите пароль')
    bot.register_next_step_handler(response, send_encrypt_pdf_file)


@update_UserState_action
def send_encrypt_pdf_file(message: Message):
    """Получения пароля для шифрования, шифрование файла, отправка файла пользователю"""
    chat_id = message.chat.id
    password = message.text

    path_to_download_file, path_to_protect_file = download_file_in_dir(message)

    pdf_writer = PdfFileWriter()
    pdf = PdfFileReader(path_to_download_file)

    for page in range(pdf.numPages):
        pdf_writer.add_page(pdf.pages[page])

    pdf_writer.encrypt(password)
    with open(path_to_protect_file, 'wb') as protect_file:
        pdf_writer.write(protect_file)
        bot.send_document(chat_id, protect_file)
        bot.send_message(chat_id, 'Ваш зашифрованный файл')


def get_name_extension(file_path):
    dir_file, name_extension = os.path.split(file_path)
    name_file, extension_file = os.path.splitext(name_extension)
    return name_file, extension_file


def download_file_in_dir(message: Message):
    chat_id = message.chat.id

    name_download_file = f'{chat_id}_{UserState.username}_{UserState.unic_pdf_name}.pdf'
    name_protect_file = f'{chat_id}_{UserState.username}_{UserState.unic_pdf_name}_protect.pdf'
    name_dir_with_files_user = f'{UserState.username}'

    abs_path_dir_with_download_files = os.path.abspath(
        os.path.join(
            'handlers', 'project_encrpyt_pdf_files', 'download_files', name_dir_with_files_user
        )
    )

    abs_path_download_file = os.path.join(abs_path_dir_with_download_files, name_download_file)
    abs_path_protect_file = os.path.join(abs_path_dir_with_download_files, name_protect_file)

    if not os.path.isdir(abs_path_dir_with_download_files):
        os.makedirs(abs_path_dir_with_download_files)

    with open(abs_path_download_file, 'wb') as pdf_file:
        pdf_file.write(UserState.pdf_file_user)

    return abs_path_download_file, abs_path_protect_file
