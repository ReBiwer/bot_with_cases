from loader import bot, bugreport_bot
import handlers
from utils.set_bot_commands import set_default_commands
from telebot.custom_filters import StateFilter

if __name__ == "__main__":
    bot.add_custom_filter(StateFilter(bot))
    bugreport_bot.add_custom_filter(StateFilter(bugreport_bot))
    set_default_commands(bot)
    bot.infinity_polling()
    bugreport_bot.infinity_polling()
