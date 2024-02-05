from database.logging import User
from datetime import datetime
from states.getting_weather import GettingWeather


def log_action(action):
    user = User(id_user=GettingWeather.id_user,
                username=GettingWeather.username_user,
                action=action,
                time_action=datetime.now(),
                )
    user.save()
