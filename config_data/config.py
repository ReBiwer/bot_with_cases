import os
from dotenv import load_dotenv, find_dotenv

if not find_dotenv('.env.template'):
    exit("Переменные окружения не загружены т.к отсутствует файл .env")
else:
    load_dotenv('.env.template')

BOT_TOKEN = os.getenv("BOT_TOKEN")
RAPID_API_KEY = os.getenv("RAPID_API_KEY")
DEFAULT_COMMANDS = (
    ("start", "Запустить бота"),
    ("help", "Вывести справку")
)
