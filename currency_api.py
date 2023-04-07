import requests
import settings_bot

def get_currency_rate():

    # Get all currency
    get_rates = requests.get(settings_bot.rates)

    # Check status code
    if get_rates.status_code != 200:
        return "⛔️Currency rate"

    # Dictionary emoji
    currency_emoji = {
        'USD': '🇺🇸',
        'EUR': '🇪🇺',
        'RUB': '🇷🇺'
    }

    # Get only USD / EUR / RUB

    # Variable where we will write the result
    currency_rates = []

    # Cycle for currency
    for message in get_rates.json():
        # Find only USD / EUR / RUB
        if message['Cur_Abbreviation'] in ['USD', 'EUR', 'RUB']:
            # Find rates
            rate = round(message['Cur_OfficialRate'], 2)
            # Add emoji
            currency_abbreviation = f"{currency_emoji[message['Cur_Abbreviation']]} {message['Cur_Abbreviation']}"
            # Save in variable Abbreviation + rate
            currency_rates.append(f"{currency_abbreviation}: {rate}")

    return "\n".join(currency_rates)

print(get_currency_rate())