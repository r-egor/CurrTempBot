import requests
import settings_bot

def get_crypto_prices():
    # Get Crypto
    get_crypto = requests.get(settings_bot.crypto)
    data = get_crypto.json()

    if get_crypto.status_code == 200:
        # BTC
        bitcoin_price = str(data["bitcoin"]["usd"]//1000) + "k"
        # ETH
        ethereum_price = str(round(data["ethereum"]["usd"]/1000, 2)) + "k"
        # TON
        the_open_network = data["the-open-network"]["usd"]

        # Message
        message_text = f"📈BTC: {bitcoin_price}|" \
                       f"ETH: {ethereum_price}|" \
                       f"TON: {the_open_network}"
    else:
        message_text = "⛔️Crypto"

    return message_text


