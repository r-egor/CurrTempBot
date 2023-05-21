import requests
import emoji_bot
from dotenv import load_dotenv
from database import DatabaseUsers
import os

load_dotenv('.env')

def get_currency_rate():
    database = DatabaseUsers()

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
            # Add abbreviation
            currency_abbreviation = f"{message['Cur_Abbreviation']}"
            # Get previous rate for the currency
            previous_rate = database.get_previous_rate(currency_abbreviation)

            # Save to database
            database = DatabaseUsers()
            database.insert_currency_data(currency_abbreviation, rate)

            # Add emoji
            currency_emoji_abbreviation = f"{emoji[message['Cur_Abbreviation']]} {currency_abbreviation}"

            # Compare rates and add arrow emoji if changed
            if previous_rate is not None:
                previous_rate = float(previous_rate)
                if rate > previous_rate:
                    rate = f"{rate} ⬆️"
                elif rate < previous_rate:
                    rate = f"{rate} ⬇️"

            # Save in variable Abbreviation + rate
            currency_rates.append(f"{currency_emoji_abbreviation}: {rate}")


    return "\n".join(currency_rates)