import requests
from services import emoji_bot
from dotenv import load_dotenv
from services.database import DatabaseUsers
import os
import time

load_dotenv('../.env')

class CurrencyRate:

    def __init__(self):
        self.database = DatabaseUsers()

    def get_currency_rate(self):

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
                previous_rate = self.database.get_previous_rate(currency_abbreviation)

                # Add emoji
                currency_emoji_abbreviation = f"{emoji[message['Cur_Abbreviation']]} {currency_abbreviation}"

                # Compare rates and add arrow emoji if changed
                if previous_rate is not None:
                    previous_rate = float(previous_rate)
                    if rate > float(previous_rate):
                        rate = f"{rate} ⬆️"
                    elif rate < float(previous_rate):
                        rate = f"{rate} ⬇️"

                # Save in variable Abbreviation + rate
                currency_rates.append(f"{currency_emoji_abbreviation}: {rate}")

        return "\n".join(currency_rates)

    def get_currency_for_database(self):

        # Get all currency
        get_rates = requests.get(os.getenv('rates'))

        # Check status code
        if get_rates.status_code != 200:
            time.sleep(900)
            return self.get_currency_for_database()

        # Cycle for currency
        for message in get_rates.json():
            # Find only USD / EUR / RUB
            if message['Cur_Abbreviation'] in ['USD', 'EUR', 'RUB']:
                # Find rates
                rate = round(message['Cur_OfficialRate'], 2)
                # Add abbreviation
                currency_abbreviation = f"{message['Cur_Abbreviation']}"

                # Save to database
                self.database.insert_currency_data(currency_abbreviation, rate)

        return
