from telebot.types import CallbackQuery
from handlers.custom_func.photo_dog import get_photo_dog
from loader import bot
from handlers.custom_func.name_now_city import get_name_now_city
from handlers.custom_func.weather_detection import weather_detection
from handlers.custom_func.weather_in_city import get_weather
from states.getting_weather import GettingWeather
from handlers.custom_func.log_func import log_action
from states.user_state import UserState


@bot.callback_query_handler(func=lambda call: call.data == 'weather_user_city', states=UserState)
def weather_now_city(call: CallbackQuery):
    """Получение текущего города пользователя и вывод погоды в его городе"""
    message = call.message
    UserState.action = GettingWeather()
    UserState.action.downloads = get_photo_dog()
    res_city_username = UserState.action.city_username = get_name_now_city()  # получаем имя города пользователя
    log_action('state=UserState, action=GettingWeather.\n'
               f'Отправлены GET запросы на получение фотографии песика и города пользователя', message)
    if res_city_username != 'Не удалось получить имя вашего текущего города':
        data_about_weather = get_weather(res_city_username)  # получаем информацию о погоде в городе
        log_action(f'state=UserState, action=GettingWeather.\n'
                   f'Получен город пользователя ({res_city_username})', message)
        if data_about_weather != 'Не удалось получить информацию о погоде в городе':
            info_about_weather = weather_detection(data_about_weather)  # обрабатываем информацию о погоде в городе
            bot.send_message(message.chat.id, info_about_weather[0])
            bot.send_message(message.chat.id, info_about_weather[1])
            log_action('state=UserState, action=GettingWeather.\n'
                       'Информация о погоде получена', message)

            if isinstance(UserState.action.downloads, str):
                bot.send_message(message.chat.id, UserState.action.downloads)
                log_action(f'state=UserState, action=GettingWeather.\n'
                           f'Фотография не была получена, {UserState.action.downloads}', message)
            else:
                bot.send_photo(message.chat.id, UserState.action.downloads)
                log_action('state=UserState, action=GettingWeather.\n'
                           'Фотография с песиком успешно получена', message)
        else:
            bot.send_message(message.chat.id, data_about_weather)
            log_action(f'state=UserState, action=GettingWeather.\n'
                       f'Информация о погоде в городе не была получена: {data_about_weather}', message)
    else:
        bot.send_message(message.chat.id, res_city_username)
        log_action(f'state=UserState, action=GettingWeather.\n'
                   f'Не удалось получить название города пользователя: {res_city_username}', message)
