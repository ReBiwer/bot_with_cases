from telebot.types import Message, CallbackQuery

from handlers.custom_func.decorators import update_UserState_action
from loader import bot
from keyboards.inline.yes_no_inline import yes_no_keyboard_inline
from handlers.project_weather.funcs.weather_in_city import get_weather
from handlers.project_weather.funcs.weather_detection import weather_detection
from handlers.project_weather.funcs.photo_dog import get_photo_dog
from handlers.custom_func.log_func import log_action
from states.user_state import UserState


@bot.callback_query_handler(func=lambda call: call.data == 'another_city')
@update_UserState_action
def weather_another_city(call: CallbackQuery):
    message = call.message
    log_action('Команда - "weather_another_city"', message)
    UserState.downloads = get_photo_dog(message)
    response_admin = bot.send_message(message.chat.id, 'Введите город где вы хотите узнать погоду')
    bot.register_next_step_handler(response_admin, put_weather)


@update_UserState_action
def put_weather(message: Message):
    city = message.text.strip().lower()
    log_action(f'Команда - "put_weather", город - {city}', message)
    data_about_weather = get_weather(city, message)
    if data_about_weather != 'Не удалось получить информацию о погоде в городе':
        info_about_weather = weather_detection(data_about_weather, city)
        bot.send_message(message.chat.id, info_about_weather[0])
        bot.send_message(message.chat.id, info_about_weather[1])

        if isinstance(UserState.downloads, str):
            bot.send_message(message.chat.id, UserState.downloads)
        else:
            bot.send_photo(message.chat.id, UserState.downloads)

        bot.send_message(message.chat.id, 'Хотите узнать погоду в другом городе?',
                         reply_markup=yes_no_keyboard_inline())
    else:
        bot.send_message(message.chat.id, data_about_weather)


@bot.callback_query_handler(func=lambda call: call.data == 'да')
@update_UserState_action
def get_weather_again(call):
    message = call.message
    log_action('Команда - рестарт команды "put_weather"', message)
    UserState.downloads = get_photo_dog(message)
    response_admin = bot.send_message(message.chat.id, 'Снова введите город где вы хотите узнать погоду')
    bot.register_next_step_handler(response_admin, put_weather)
