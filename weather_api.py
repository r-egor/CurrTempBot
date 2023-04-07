import requests
import settings_bot

def get_weather_forecast():
    # Get weather
    brest_weather = requests.get(settings_bot.brest_weather)
    brest = brest_weather.text

    vitebsk_weather = requests.get(settings_bot.vitebsk_weather)
    vitebsk = vitebsk_weather.text

    gomel_weather = requests.get(settings_bot.gomel_weather)
    gomel = gomel_weather.text

    grodno_weather = requests.get(settings_bot.grodno_weather)
    grodno = grodno_weather.text

    minsk_weather = requests.get(settings_bot.minsk_weather)
    minsk = minsk_weather.text

    mogilev_weather = requests.get(settings_bot.mogilev_weather)
    mogilev = mogilev_weather.text

    if brest_weather.status_code == 200 and vitebsk_weather.status_code ==200\
            and gomel_weather.status_code == 200 and grodno_weather.status_code == 200\
            and minsk_weather.status_code == 200 and mogilev_weather.status_code ==200:

        # Message Minsk
        message_text = f'{brest}' \
                       f'{vitebsk}' \
                       f'{gomel}'\
                       f'{grodno}'\
                       f'{minsk}'\
                       f'{mogilev}'\

    else:
        message_text = "⛔️Weather"

    return message_text

print(get_weather_forecast())