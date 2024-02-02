import json


def weather_now_city_detection(data_for_weather: json) -> str:
    id_list_good_weather = [800, 801, 802, 600, 601]
    temp_in_city = data_for_weather['main']['temp']
    description_weather_in_city = data_for_weather['weather'][0]['description']
    if data_for_weather['weather'][0]['id'] in id_list_good_weather:
        return (f'Погода в вашем городе хорошая:\n'
                f'{description_weather_in_city} {temp_in_city}')
    else:
        return (f'Погода в вашем городе не очень:\n'
                f'{description_weather_in_city} {temp_in_city}')


def weather_another_city_detection(data_for_weather: json, city: str) -> str:
    id_list_good_weather = [800, 801, 802, 600, 601]
    temp_in_city = data_for_weather['main']['temp']
    description_weather_in_city = data_for_weather['weather'][0]['description']
    if data_for_weather['weather'][0]['id'] in id_list_good_weather:
        return (f'Погода в городе {city} хорошая:\n'
                f'{description_weather_in_city} {temp_in_city}')
    else:
        return (f'Погода в городе {city} не очень:\n'
                f'{description_weather_in_city} {temp_in_city}')
