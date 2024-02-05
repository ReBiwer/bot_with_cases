from telebot.types import Message
from handlers.custom_func.log_func import log_action
from config_data.config import DEFAULT_COMMANDS
from loader import bot
from keyboards.inline.select_city import keyboard_selecе_city
from states.getting_weather import GettingWeather
from handlers.custom_func.photo_dog import get_photo_dog


@bot.message_handler(commands=["help"])
def bot_help(message: Message):
    log_action('commands=["help"]')
    GettingWeather.id_user = message.from_user.id
    GettingWeather.username_user = message.from_user.username
    GettingWeather.downloads = get_photo_dog()
    bot.send_message(message.chat.id, 'Этот бот предназанчен для получения погоды\n'
                                      'В вашем городе или в любом другом, в каком только захотите')
    bot.send_message(message.chat.id, 'Выберите где вы хотите узнать погоду', reply_markup=keyboard_selecе_city())
