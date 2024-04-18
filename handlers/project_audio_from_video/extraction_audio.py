from moviepy import editor
from telebot.types import CallbackQuery, Message
from handlers.custom_func.decorators import update_UserState_action
from handlers.custom_func.log_func import log_action
from keyboards.inline.restart import restart_button
from loader import bot
import os


@bot.callback_query_handler(func=lambda call: call.data == 'extract_audio')
@update_UserState_action
def start_extract_audio(call: CallbackQuery):
    """
    Старт проекта 'аудио из видео'
    """
    message = call.message
    log_action('Старт извлечения аудио. Запрос видео для обработки', message)
    response = bot.send_message(message.chat.id, 'Загрузите видео из которого вы хотите извлечь аудио')
    bot.register_next_step_handler(response, extraction_audio)


@update_UserState_action
def extraction_audio(message: Message):
    log_action('Начало обработки видео.', message)
    bot.send_message(message.chat.id, 'Идет обработка файла, подождите немного...')
    chat_id = message.chat.id
    path_video_from_mes = bot.get_file(message.video.file_id).file_path
    download_video = bot.download_file(path_video_from_mes)
    path_dir = os.path.abspath(os.path.join('handlers', 'project_audio_from_video', 'download_files', f'{chat_id}'))
    filename_video = f'{path_dir}\\{chat_id}_video.mp4'
    filename_audio = f'{path_dir}\\{chat_id}_video.mp3'

    if not os.path.isdir(path_dir):
        os.mkdir(path_dir)

    with open(filename_video, 'wb') as file:
        file.write(download_video)

    video_file = editor.VideoFileClip(filename_video)
    video_file.audio.write_audiofile(filename_audio)

    with open(filename_audio, 'rb') as audio:
        bot.send_document(chat_id, audio)

    bot.send_message(chat_id, 'Прошу, вот ваш файл', reply_markup=restart_button())
    log_action('Аудио было извлечено успешно', message)
