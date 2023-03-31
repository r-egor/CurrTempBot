import requests
import settings_bot

def get_currency_rate():
    # Get USD
    get_usd = requests.get(settings_bot.usd)
    data_usd = get_usd.json()

    cur_abbreviation_usd = data_usd['Cur_Abbreviation']
    cur_official_rate_usd = data_usd['Cur_OfficialRate']

    # Get EUR
    get_eur = requests.get(settings_bot.eur)
    data_eur = get_eur.json()

    cur_abbreviation_eur = data_eur['Cur_Abbreviation']
    cur_official_rate_eur = data_eur['Cur_OfficialRate']

    # Get RUB
    get_rub = requests.get(settings_bot.rub)
    data_rub = get_rub.json()

    cur_abbreviation_rub = data_rub['Cur_Abbreviation']
    cur_official_rate_rub = data_rub['Cur_OfficialRate']

    # Message
    message_text = f"🇺🇸 {cur_abbreviation_usd}: {cur_official_rate_usd}\n"\
                   f"🇪🇺 {cur_abbreviation_eur}: {cur_official_rate_eur}\n" \
                   f"🇷🇺 {cur_abbreviation_rub}: {cur_official_rate_rub}"

    return message_text

print(get_currency_rate())