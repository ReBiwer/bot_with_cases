import pyAesCrypt
import os
from telebot.types import CallbackQuery, Message
from handlers.custom_func.decorators import update_UserState_action
from keyboards.inline.restart import restart_button
from loader import bot
from states.user_state import UserState


@bot.callback_query_handler(func=lambda call: call.data == "encrypt_file")
@update_UserState_action
def request_file_for_encryption(call: CallbackQuery):
    """Запрашиваем файл, который пользователь хочет зашифровать"""
    message = call.message
    UserState.current_logger.info('Запрос файла для шифрования')
    response = bot.send_message(message.chat.id, 'Загрузите файл, который вы хотите зашифровать.')
    bot.register_next_step_handler(response, get_file_for_encryption)


@update_UserState_action
def get_file_for_encryption(message: Message):
    """Получаем файл, который нужно зашифровать и запрашиваем пароль для шифрования"""
    UserState.current_logger.info('Получение файла для шифрования. Запрос пароля')
    chat_id = message.chat.id
    path_file = get_file_path(message)
    UserState.path_to_file_for_encryption = path_file
    response = bot.send_message(chat_id, 'Прошу введите пароль. '
                                         'Он понадобиться, когда вы захотите дешифровать свой файл'
                                )
    bot.register_next_step_handler(response, send_encryption_file)


@update_UserState_action
def send_encryption_file(message: Message):
    """
    Получаем пароль для дешифровки файла и скидываем зашифрованный файл.
    P.S. написать пользователю, чтобы название файла не изменял
    """
    UserState.current_logger.info('Пароль был получен. Начало обработки файла')

    #  Получаем пароль, ID чата и сохраняем пароль в атрибуте UserState для сохранения
    password: str = message.text
    chat_id: int = message.chat.id
    UserState.password_for_decryption_file = password

    #  Скачиваем файл
    download_file_for_encryption: bytes = bot.download_file(UserState.path_to_file_for_encryption)

    #  Получаем директорию файла, имя файла и расширение файла
    dir_to_file, filename, file_extension = get_dir_name_extension_file(UserState.path_to_file_for_encryption)
    UserState.extension_decrypt_file = file_extension
    #  Создаем путь к директории где будет храниться скаченный файл
    path_dir: str = os.path.abspath(
        os.path.join(
            'handlers',
            'project_file_encryption',
            'download_files',
            f'encrypt_{dir_to_file}_{UserState.username}'
        )
    )
    path_to_file: str = os.path.join(path_dir, f'{chat_id}_{filename}{file_extension}')
    path_to_encrypt_file = os.path.join(path_dir, f'{chat_id}_{filename}.aes')
    UserState.path_to_file_for_encryption = path_to_encrypt_file

    if not os.path.isdir(path_dir):
        UserState.current_logger.info('Создание директории с файлами пользователя')
        os.makedirs(path_dir)

    with open(path_to_file, 'wb') as file:
        file.write(download_file_for_encryption)
        UserState.current_logger.info('Сохранение полученного файла')

    UserState.current_logger.info('Начало шифрования файла')
    pyAesCrypt.encryptFile(path_to_file, path_to_encrypt_file, password)
    UserState.current_logger.info('Конец шифрования файла')

    with open(path_to_encrypt_file, 'rb') as encrypt_file:
        bot.send_document(chat_id, encrypt_file)
        UserState.current_logger.info('Зашифрованный файл был отправлен')

    bot.send_message(
        chat_id,
        "Прошу, ваш зашифрованный файл. "
        "Просьба не изменять название и расширение файла, "
        "если вы хотите в дальнейшем дешифровать ваш файл",
        reply_markup=restart_button()
    )


@bot.callback_query_handler(func=lambda call: call.data == "decrypt_file")
@update_UserState_action
def request_encryption_file(call: CallbackQuery):
    """
    Получаем зашифрованный файл и запрашиваем пароль для дешифровки.
    P.S. написать пользователю, что имя файла должно быть таким же, какое было присвоено этим ботом
    """
    message = call.message
    UserState.current_logger.info('Запрос файла для дешифрования')
    response = bot.send_message(message.chat.id, 'Загрузите файл, который вы хотите дешифровать.')
    bot.register_next_step_handler(response, get_password_for_decryption)


@update_UserState_action
def get_password_for_decryption(message: Message):
    """Получаем зашифрованный файл и запрашиваем пароль для дешифрования"""
    UserState.current_logger.info('Получение файла для дешифрования. Запрос пароля')
    chat_id = message.chat.id
    path_file = get_file_path(message)

    dir_file, name_file, extension_file = get_dir_name_extension_file(path_file)
    path_dir = os.path.abspath(
        os.path.join(
            'handlers',
            'project_file_encryption',
            'download_files',
            f'decrypt_{dir_file}_{UserState.username}'
        )
    )

    if not os.path.isdir(path_dir):
        UserState.current_logger.info('Создание директории с файлами пользователя')
        os.makedirs(path_dir)

    path_to_decrypt_file: str = os.path.join(path_dir, f'{chat_id}_{name_file}{extension_file}')
    UserState.path_to_file_for_decryption = path_to_decrypt_file
    download_file = bot.download_file(path_file)
    with open(path_to_decrypt_file, 'wb') as file:
        file.write(download_file)

    response = bot.send_message(chat_id, 'Введите пароль для дешифровки файла')
    bot.register_next_step_handler(response, send_decryption_file)


@update_UserState_action
def send_decryption_file(message: Message):
    """Получаем пароль для дешифровки файла, дешифруем файл и отправляем пользователю"""
    UserState.current_logger.info('Отправка дешифрованного файла')
    chat_id = message.chat.id
    password = message.text
    path_to_decrypt_file, extension_to_decrypt_file = os.path.splitext(UserState.path_to_file_for_decryption)
    path_to_result_file = f'{path_to_decrypt_file}.{UserState.extension_decrypt_file}'
    if password == UserState.password_for_decryption_file:
        pyAesCrypt.decryptFile(UserState.path_to_file_for_decryption,
                               path_to_result_file,
                               password
                               )
        with open(path_to_result_file) as decrypt_file:
            bot.send_document(chat_id, decrypt_file)
            UserState.current_logger.info('Дешифрованный файл был отправлен')
        bot.send_message(chat_id, 'Прошу, ваш дешифрованный файл', reply_markup=restart_button())


def get_file_path(message: Message) -> str:
    """Получаем путь к файлу для скачивания в зависимости от типа отправленного файла"""
    if message.document:
        path_file = bot.get_file(message.document.file_id).file_path
    elif message.video:
        path_file = bot.get_file(message.video.file_id).file_path
    else:
        path_file = bot.get_file(message.photo[-1].file_id).file_path
    UserState.debug_logger.debug(f'Путь для скачивания файла: {path_file}')
    return path_file


def get_dir_name_extension_file(path_file: str) -> tuple[str, str, str]:
    """Разделяем путь к файлу на директорию, имя и расширение"""
    dir_and_name, file_extension = os.path.splitext(path_file)
    file_dir, file_name = os.path.split(dir_and_name)
    UserState.debug_logger.debug(f'file_dir: {file_dir}, '
                                 f'file_name: {file_name}, '
                                 f'file_extension: {file_name}')
    return file_dir, file_name, file_extension
