import logging.config
from logging import Logger
from telebot import TeleBot
from database.list_admins import Admins
from telebot.types import Message
from pathlib import Path


def get_logger(name_user: str, id_user: int) -> Logger:
    dict_config: dict = get_dict_config(name_user, id_user)
    logging.config.dictConfig(dict_config)
    logger: Logger = logging.getLogger(f'Пользователь: {name_user} ({id_user})')
    return logger


def get_dict_config(name_user: str, id_user: int):
    path_to_file = Path(f'handlers/custom_func/logs/{name_user}_{id_user}.txt')
    dict_config = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "simple": {
                "format": "%(name)s | %(asctime)s | %(message)s",
            }
        },
        "handlers": {
            "base_handler": {
                "class": "logging.handlers.TimedRotatingFileHandler",
                "when": "h",
                "interval": 10,
                "backupCount": 5,
                "level": "INFO",
                "formatter": "simple",
                "filename": path_to_file,
                "encoding": "utf-8",
            }
        },
        "loggers": {
            f'Пользователь: {name_user} ({id_user})': {
                "level": "INFO",
                "handlers": ["base_handler"]
            },
        },
    }
    return dict_config


def put_log_info(bot_rep: TeleBot, message: Message):
    name_user = message.chat.username if message.chat.username else message.chat.first_name
    id_user = message.chat.id
    user_report = message.text
    #  Путь к файлу с логами пользователя
    path_to_file = Path(f'handlers/custom_func/logs/{name_user}_{id_user}.txt')
    #  ID всех админов для отправки сообщения о новом репорт
    id_admins = [admin.id_admin for admin in Admins.select()]
    with open(path_to_file, encoding='utf-8') as log_file:
        for id_chat in id_admins:
            bot_rep.send_message(id_chat, 'Пришел новый репорт')
            bot_rep.send_message(id_chat, f'Пользователь: {name_user}\n'
                                          f'id пользователя: {id_user}\n'
                                          f'Сообщение: {user_report}')
            bot_rep.send_document(id_chat, log_file)
