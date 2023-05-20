import requests
import emoji_bot
from dotenv import load_dotenv
from database import DatabaseUsers
import os

load_dotenv('.env')

def get_currency_rate():

    # Get all currency
    get_rates = requests.get(os.getenv('rates'))

    # Check status code
    if get_rates.status_code != 200:
        return "⛔️Currency rate"

    # Dictionary emoji
    emoji = emoji_bot.currency_emoji

    # Variable where we will write the result
    currency_rates = []

    # Cycle for currency
    for message in get_rates.json():
        # Find only USD / EUR / RUB
        if message['Cur_Abbreviation'] in ['USD', 'EUR', 'RUB']:
            # Find rates
            rate = round(message['Cur_OfficialRate'], 2)
            # Add emoji
            currency_abbreviation = f"{emoji[message['Cur_Abbreviation']]} {message['Cur_Abbreviation']}"
            # Save in variable Abbreviation + rate
            currency_rates.append(f"{currency_abbreviation}: {rate}")
            # Save to database
            database = DatabaseUsers()
            database.insert_currency_data(currency_abbreviation, rate)

    return "\n".join(currency_rates)