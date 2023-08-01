import requests
from services import emoji_bot
from dotenv import load_dotenv
import os

load_dotenv('../.env')


class Weather_forecast:

    def __init__(self):
        self.base_urls = {
            'main': os.getenv('base_url'),
            'brest': os.getenv('base_url_brest_reg'),
            'vitebsk': os.getenv('base_url_vitebsk_reg'),
            'gomel': os.getenv('base_url_gomel_reg'),
            'grodno': os.getenv('base_url_grodno_reg'),
            'minsk': os.getenv('base_url_minsk_reg'),
            'mogilev': os.getenv('base_url_mogilev_reg')
        }

    def get_weather(self, region):

        # Getting a value from a dictionary
        base_url = self.base_urls.get(region)

        # Get weather data
        response = requests.get(base_url)

        # Check status code
        if response.status_code != 200:
            return "⛔️ Weather"

        # Emoji for weather - main
        emoji = emoji_bot.weather_emoji

        data = response.json()

        # Variable where we will write the result
        weather_forecast = []

        for city in data['list']:
            # Add emoji
            weather_emoji = f"{emoji.get(city['weather'][0]['main'], ' ')}"
            # Save in variable City + Temp
            weather_forecast.append(f"{city['name']}: {weather_emoji} 🌡️{round(city['main']['temp'])}°C "
                                    f"👤{round(city['main']['feels_like'])}°C")

        return "\n".join(weather_forecast)
