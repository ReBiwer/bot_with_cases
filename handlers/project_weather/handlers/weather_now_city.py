from telebot.types import CallbackQuery

from handlers.custom_func.decorators import update_UserState_action
from handlers.project_weather.funcs.photo_dog import get_photo_dog
from keyboards.inline.restart import restart_button
from loader import bot
from handlers.project_weather.funcs.name_now_city import get_name_now_city
from handlers.project_weather.funcs.weather_detection import weather_detection
from handlers.project_weather.funcs.weather_in_city import get_weather
from states.user_state import UserState


@bot.callback_query_handler(func=lambda call: call.data == 'weather_user_city')
@update_UserState_action
def weather_user_city(call: CallbackQuery):
    """Получение текущего города пользователя и вывод погоды в его городе"""
    message = call.message
    UserState.current_message = message
    UserState.downloads = get_photo_dog(message)
    res_city_username = UserState.city_username = get_name_now_city(message)  # получаем имя города пользователя
    if res_city_username != 'Не удалось получить имя вашего текущего города':
        data_about_weather = get_weather(res_city_username, message)  # получаем информацию о погоде в городе
        if data_about_weather != 'Не удалось получить информацию о погоде в городе':
            info_about_weather = weather_detection(data_about_weather)  # обрабатываем информацию о погоде в городе
            bot.send_message(message.chat.id, info_about_weather[0])
            bot.send_message(message.chat.id, info_about_weather[1])

            if isinstance(UserState.downloads, str):
                bot.send_message(message.chat.id, UserState.downloads)
            else:
                bot.send_photo(message.chat.id, UserState.downloads)
        else:
            bot.send_message(message.chat.id, data_about_weather)
    else:
        bot.send_message(message.chat.id, res_city_username)
    bot.send_message(message.chat.id, 'Вернуться к выбору кейсов', reply_markup=restart_button())
