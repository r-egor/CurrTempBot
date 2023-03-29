import requests

def get_currency_rate():
    # Get USD
    get_usd = requests.get("https://www.nbrb.by/api/exrates/rates/431")
    data_usd = get_usd.json()

    cur_abbreviation_usd = data_usd['Cur_Abbreviation']
    cur_official_rate_usd = data_usd['Cur_OfficialRate']

    # Get EUR
    get_eur = requests.get("https://www.nbrb.by/api/exrates/rates/451")
    data_eur = get_eur.json()

    cur_abbreviation_eur = data_eur['Cur_Abbreviation']
    cur_official_rate_eur = data_eur['Cur_OfficialRate']

    # Get RUB

    get_rub = requests.get("https://www.nbrb.by/api/exrates/rates/456")
    data_rub = get_rub.json()

    cur_abbreviation_rub = data_rub['Cur_Abbreviation']
    cur_official_rate_rub = data_rub['Cur_OfficialRate']

    # Message

    message_text = f"🇺🇸 {cur_abbreviation_usd}: {cur_official_rate_usd} "\
                   f"🇪🇺 {cur_abbreviation_eur}: {cur_official_rate_eur} " \
                   f"🇷🇺 {cur_abbreviation_rub}: {cur_official_rate_rub}"

    return message_text
