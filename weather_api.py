import requests
import settings_bot


def get_weather_forecast():

    # Get weather in Brest, Vitebsk, Gomel, Grodno, Minsk, Mogilev
    get_weather = requests.get(settings_bot.base_url, settings_bot.params)

    # Check status code
    if get_weather.status_code != 200:
        return "⛔️Weather"

    data = get_weather.json()

    # Variable where we will write the result
    weather_forecast = []

    for city in data['list']:
            # Save in variable City + Temp
            weather_forecast.append(f"{city['name']}: 🌡️{round(city['main']['temp'])}°C")

    return "\n".join(weather_forecast)