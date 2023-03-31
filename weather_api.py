import requests
import settings_bot
from translate import Translator

def get_weather_forecast():
    # Get weather
    get_weather = requests.get(settings_bot.weather)
    data = get_weather.text.split('\n')

    if get_weather.status_code ==200:
        # Weather description
        weather_desc = data[0]
        # Temperature
        current_temp = data[1]
        night_temp = data[2]

        # Translate weather description in ru
        translator = Translator(to_lang="ru")
        weather_desc_rus = translator.translate(weather_desc)

        # Message Minsk
        message_text = f'Погода в Минске:\n' \
                       f'{weather_desc_rus} ' \
                       f'🌝 {current_temp} ' \
                       f'🌚 ({night_temp})'
    else:
        message_text = "⛔Weather"

    return message_text

