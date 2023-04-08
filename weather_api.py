import requests
import settings_bot


def get_weather_forecast():

    # Get weather in Brest, Vitebsk, Gomel, Grodno, Minsk, Mogilev
    get_weather = requests.get(settings_bot.base_url, settings_bot.params)

    # Check status code
    if get_weather.status_code != 200:
        return "⛔️Weather"

    # Emoji for weather - main
    emoji = {
        'Clouds': '☁️',
        'Clear': '☀️',
        'Rain': '☔️',
        'Snow': '❄️',
        'Fog': '🌫️',
        'Thunderstorm': '⛈️',
        'Drizzle': '🌧️',
        'Squall': '🌬️'
    }

    data = get_weather.json()

    # Variable where we will write the result
    weather_forecast = []

    for city in data['list']:
            # Add emoji
            weather_emoji = f"{emoji[city['weather'][0]['main']]}"
            # Save in variable City + Temp
            weather_forecast.append(f"{city['name']}: {weather_emoji} 🌡️{round(city['main']['temp'])}°C "
                                    f"👤{round(city['main']['feels_like'])}°C")

    return "\n".join(weather_forecast)