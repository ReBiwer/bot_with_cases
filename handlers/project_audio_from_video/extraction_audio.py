from moviepy import editor
from telebot.types import CallbackQuery, Message

from handlers.custom_func.decorators import update_UserState_action
from loader import bot


@bot.callback_query_handler(func=lambda call: call.data == 'extract_audio')
@update_UserState_action
def start_extract_audio(call: CallbackQuery):
    """
    Старт проекта 'аудио из видео'
    """
    message = call.message
    response = bot.send_message(message.chat.id, 'Загрузите видео из которого вы хотите извлечь аудио')
    bot.register_next_step_handler(response, extraction_audio)


@update_UserState_action
def extraction_audio(message: Message):
    bot.send_message(message.chat.id, 'Идет обработка файла, подождите немного...')
    path_video_from_mes = bot.get_file(message.video.file_id).file_path
    download_video = bot.download_file(path_video_from_mes)
    with open(f'video_{message.chat.id}.mp4', 'wb') as file:
        file.write(download_video)
    video_file = editor.VideoFileClip(f'video_{message.chat.id}.mp4')
    video_file.audio.write_audiofile('audio_from_video.mp3')
    bot.send_message(message.chat.id, 'Прошу, вот ваш файл')
    with open('audio_from_video.mp3', 'rb') as audio:
        bot.send_document(message.chat.id, audio)
