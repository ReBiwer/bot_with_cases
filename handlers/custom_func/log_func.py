from telebot import TeleBot

from database.list_admins import Admins
from database.logging_users import UserAction
from database.logging_admins import AdminAction
from datetime import datetime
from telebot.types import Message, CallbackQuery


def log_action(action, message: Message | CallbackQuery, check_admin=False):
    if check_admin:
        admin_action = AdminAction.create(id_admin=message.chat.id,
                                          username_admin=message.chat.username,
                                          action_admin=action,
                                          time_action=datetime.now(),
                                          )
        admin_action.save()
    else:
        user_action = UserAction.create(id_user=message.chat.id,
                                        username=message.chat.username,
                                        action=action,
                                        time_action=datetime.now(),
                                        )
        user_action.save()


def put_log_info(bot: TeleBot, message: Message, check_admin=False):
    if check_admin:
        pass
    else:
        id_user = message.from_user.id
        username = message.from_user.username
        user_report = message.text
        actions_user = ''
        for user in UserAction.select().where(UserAction.id_user == id_user):
            actions_user += (f'ID_user: {user.id_user} -- '
                             f'username: {user.username} -- '
                             f'action: {user.action} -- '
                             f'time_action: {user.time_action}\n')
        id_admins = [admin.id_admin for admin in Admins.select()]
        with open(f'handlers/custom_func/logs/{id_user}_logfile.log', 'w') as log_file:
            log_file.write(str(actions_user))
        with open(f'handlers/custom_func/logs/{id_user}_logfile.log', 'r') as log_file:
            for id_chat in id_admins:
                bot.send_message(id_chat, 'Пришел новый репорт')
                bot.send_message(id_chat, f'Пользователь: {username}\n'
                                          f'id пользователя: {id_user}\n'
                                          f'Сообщение: {user_report}')
                bot.send_document(id_chat, log_file)


dicct = {'content_type': 'text', 'id': 1376, 'message_id': 1376,
         'from_user': {'id': 437878719, 'is_bot': False, 'first_name': 'Владимир', 'username': 'ReBiwer',
                       'last_name': 'Быков', 'language_code': 'ru', 'can_join_groups': None,
                       'can_read_all_group_messages': None, 'supports_inline_queries': None, 'is_premium': None,
                       'added_to_attachment_menu': None}, 'date': 1712754120,
         'chat': {'id': 437878719, 'type': 'private', 'title': None, 'username': 'ReBiwer', 'first_name': 'Владимир',
                  'last_name': 'Быков', 'is_forum': None, 'photo': None, 'bio': None, 'join_to_send_messages': None,
                  'join_by_request': None, 'has_private_forwards': None,
                  'has_restricted_voice_and_video_messages': None, 'description': None, 'invite_link': None,
                  'pinned_message': None, 'permissions': None, 'slow_mode_delay': None,
                  'message_auto_delete_time': None, 'has_protected_content': None, 'sticker_set_name': None,
                  'can_set_sticker_set': None, 'linked_chat_id': None, 'location': None, 'active_usernames': None,
                  'emoji_status_custom_emoji_id': None, 'has_hidden_members': None,
                  'has_aggressive_anti_spam_enabled': None, 'emoji_status_expiration_date': None,
                  'available_reactions': None, 'accent_color_id': None, 'background_custom_emoji_id': None,
                  'profile_accent_color_id': None, 'profile_background_custom_emoji_id': None,
                  'has_visible_history': None}, 'sender_chat': None, 'is_automatic_forward': None,
         'reply_to_message': None, 'via_bot': None, 'edit_date': None, 'has_protected_content': None,
         'media_group_id': None, 'author_signature': None, 'text': 'hj', 'entities': None, 'caption_entities': None,
         'audio': None, 'document': None, 'photo': None, 'sticker': None, 'video': None, 'video_note': None,
         'voice': None, 'caption': None, 'contact': None, 'location': None, 'venue': None, 'animation': None,
         'dice': None, 'new_chat_members': None, 'left_chat_member': None, 'new_chat_title': None,
         'new_chat_photo': None, 'delete_chat_photo': None, 'group_chat_created': None, 'supergroup_chat_created': None,
         'channel_chat_created': None, 'migrate_to_chat_id': None, 'migrate_from_chat_id': None, 'pinned_message': None,
         'invoice': None, 'successful_payment': None, 'connected_website': None, 'reply_markup': None,
         'message_thread_id': None, 'is_topic_message': None, 'forum_topic_created': None, 'forum_topic_closed': None,
         'forum_topic_reopened': None, 'has_media_spoiler': None, 'forum_topic_edited': None,
         'general_forum_topic_hidden': None, 'general_forum_topic_unhidden': None, 'write_access_allowed': None,
         'users_shared': None, 'chat_shared': None, 'story': None, 'external_reply': None, 'quote': None,
         'link_preview_options': None, 'giveaway_created': None, 'giveaway': None, 'giveaway_winners': None,
         'giveaway_completed': None, 'forward_origin': None, 'json': {'message_id': 1376,
                                                                      'from': {'id': 437878719, 'is_bot': False,
                                                                               'first_name': 'Владимир',
                                                                               'last_name': 'Быков',
                                                                               'username': 'ReBiwer',
                                                                               'language_code': 'ru'},
                                                                      'chat': {'id': 437878719,
                                                                               'first_name': 'Владимир',
                                                                               'last_name': 'Быков',
                                                                               'username': 'ReBiwer',
                                                                               'type': 'private'}, 'date': 1712754120,
                                                                      'text': 'hj'}}
