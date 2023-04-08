import telebot
import currency_api
import coin_api
import weather_api
import settings_bot


bot = telebot.TeleBot(settings_bot.token)

@bot.message_handler(commands=['start'])
def start(message):
    # User greeting
    greeting = f'Добрый день, {message.from_user.first_name}'
    # Currency rate
    currency = currency_api.get_currency_rate()
    # Crypto price
    crypto = coin_api.get_crypto_prices()
    # Weather
    weather = weather_api.get_weather_forecast()
    # Send 'start' message
    start_message = f'{greeting}\n\n{currency}\n\n{weather}\n\n{crypto}'
    bot.send_message(message.chat.id, start_message)


bot.polling(none_stop=True)
