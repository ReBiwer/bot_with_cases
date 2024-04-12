from telebot.types import Message

from handlers.custom_func.decorators import update_UserState_action
from loader import bot
from handlers.custom_func.log_func import put_log_info


@bot.message_handler(commands=["report"])
@update_UserState_action
def get_user_report(message: Message):
    chat_id = message.chat.id
    user_report = bot.send_message(chat_id, 'Опишите что пошло не так?')
    bot.register_next_step_handler(user_report, put_user_report)


@update_UserState_action
def put_user_report(message: Message):
    chat_id = message.chat.id
    put_log_info(bot, message)
    bot.send_message(chat_id, 'Сообщение об ошибке было отправлено администраторам.\n'
                              'Спасибо за информацию в скором времени все починим:)')
