import os
from dotenv import load_dotenv, find_dotenv

if not find_dotenv('.env.template'):
    exit("Переменные окружения не загружены т.к отсутствует файл .env")
else:
    load_dotenv('.env.template')

BOT_TOKEN = os.getenv("BOT_TOKEN")
API_KEY_weather = os.getenv("API_KEY_weather")
API_KEY_get_ip = os.getenv("API_KEY_get_ip")
DEFAULT_COMMANDS = (
    ("start", "Запустить бота"),
    ("help", "Вывести справку"),
    ("report", "Сообщить об ошибке"),
)
