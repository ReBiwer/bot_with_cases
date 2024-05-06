from telebot.types import Message, CallbackQuery

from handlers.custom_func.decorators import update_UserState_action
from loader import bot
from keyboards.inline.yes_no_inline import yes_no_keyboard_inline
from handlers.project_weather.funcs.weather_in_city import get_weather
from handlers.project_weather.funcs.weather_detection import weather_detection
from handlers.project_weather.funcs.photo_dog import get_photo_dog
from states.user_state import UserState


@bot.callback_query_handler(func=lambda call: call.data == 'another_city')
@update_UserState_action
def weather_another_city(call: CallbackQuery):
    message: Message = call.message
    UserState.current_logger.info('команда - "weather_another_city"')
    UserState.downloads = get_photo_dog(message)
    response_admin = bot.send_message(message.chat.id, 'Введите город где вы хотите узнать погоду')
    bot.register_next_step_handler(response_admin, put_weather)


@update_UserState_action
def put_weather(message: Message):
    city = message.text.strip().lower()
    UserState.current_logger.info(f'команда - "put_weather", город - {city}')
    data_about_weather = get_weather(city)
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
    UserState.current_logger.info('команда - рестарт команды "put_weather"')
    UserState.downloads = get_photo_dog(message)
    response_admin = bot.send_message(message.chat.id, 'Снова введите город где вы хотите узнать погоду')
    bot.register_next_step_handler(response_admin, put_weather)
