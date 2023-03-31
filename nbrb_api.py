import requests
import settings_bot

def get_currency_rate():
    # Get USD
    get_usd = requests.get(settings_bot.usd)
    data_usd = get_usd.json()

    if get_usd.status_code == 200:

        usd_abbreviation = data_usd['Cur_Abbreviation']
        usd_official_rate = round(data_usd['Cur_OfficialRate'], 2)

        # Get EUR
        get_eur = requests.get(settings_bot.eur)
        data_eur = get_eur.json()

        eur_abbreviation = data_eur['Cur_Abbreviation']
        eur_official_rate = round(data_eur['Cur_OfficialRate'], 2)

        # Get RUB
        get_rub = requests.get(settings_bot.rub)
        data_rub = get_rub.json()

        rub_abbreviation = data_rub['Cur_Abbreviation']
        rub_official_rate = round(data_rub['Cur_OfficialRate'], 2)

        # Message
        message_text = f"🇺🇸 {usd_abbreviation}: {usd_official_rate}\n"\
                       f"🇪🇺 {eur_abbreviation}: {eur_official_rate}\n" \
                       f"🇷🇺 {rub_abbreviation}: {rub_official_rate}"
    else:
        message_text = "⛔️Currency rate"

    return message_text
