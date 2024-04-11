from telebot.types import Message, CallbackQuery
from loader import bot
from states.getting_weather import GettingWeather
from keyboards.inline.yes_no_inline import yes_no_keyboard_inline
from handlers.custom_func.weather_in_city import get_weather
from handlers.custom_func.weather_detection import weather_detection
from handlers.custom_func.photo_dog import get_photo_dog
from handlers.custom_func.log_func import log_action


@bot.callback_query_handler(func=lambda call: call.data == 'another_city')
def weather_another_city(call: CallbackQuery):
    message = call.message
    log_action('call.data = "another_city"', call)
    # bot.set_state(GettingWeather.id_user, GettingWeather.another_city)
    bot.send_message(message.chat.id, 'Введите город где вы хотите узнать погоду')


# @bot.message_handler(state=GettingWeather.another_city)
# def put_weather(message: Message):
#     log_action('state = GettingWeather.another_city', message)
#     city = message.text.strip().lower()
#     data_about_weather = get_weather(city, message)
#     if data_about_weather != 'Не удалось получить информацию о погоде в городе':
#         info_about_weather = weather_detection(data_about_weather, city)
#         bot.send_message(message.chat.id, info_about_weather[0])
#         bot.send_message(message.chat.id, info_about_weather[1])
#
#         if isinstance(GettingWeather.downloads, str):
#             bot.send_message(message.chat.id, GettingWeather.downloads)
#         else:
#             bot.send_photo(message.chat.id, GettingWeather.downloads)
#
#         bot.send_message(message.chat.id, 'Хотите узнать погоду в другом городе?',
#                          reply_markup=yes_no_keyboard_inline())
#     else:
#         bot.send_message(message.chat.id, data_about_weather)


@bot.callback_query_handler(func=lambda call: call.data == 'да')
def get_weather_again(call):
    message = call.message
    log_action('call.data = "да"', message)
    GettingWeather.downloads = get_photo_dog(message)
    bot.send_message(message.chat.id, 'Снова введите город где вы хотите узнать погоду')


@bot.callback_query_handler(func=lambda call: call.data == 'нет')
def restart(call):
    message = call.message
    log_action('call.data = "нет"', message)
    bot.delete_state(message.chat.id)
    bot.send_message(message.chat.id, 'Всего доброго:)\n'
                                      'Если хотите снова узнать погоду и поднять настроение, '
                                      'запустите бота снова через меню')
