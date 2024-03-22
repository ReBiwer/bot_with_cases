from telebot.types import Message
from loader import bot
from handlers.custom_func.log_func import log_action
from handlers.custom_func.check_admin import check_admin_status
from keyboards.inline.select_city import keyboard_selecе_city
from states.getting_weather import GettingWeather
from handlers.custom_func.photo_dog import get_photo_dog


@bot.message_handler(commands=["start"])
def bot_start(message: Message):
    chat_id = message.chat.id
    if check_admin_status(message):
        log_action('commands = ["start"]', message, check_admin=True)

        bot.send_message(chat_id, f'Приветствую вас, администратор {message.from_user.username}')
    else:
        bot.set_state(message.from_user.id, GettingWeather.id_user, chat_id)
        GettingWeather.id_user = chat_id
        GettingWeather.username_user = chat_id
        GettingWeather.downloads = get_photo_dog()
        bot.send_message(chat_id, 'Приветствую, рад вас видеть!')
        bot.send_message(chat_id, 'Хотите узнать погоду в своем городе?', reply_markup=keyboard_selecе_city())
        log_action('commands = ["start"]', message)
        bot.send_message(chat_id, message)
