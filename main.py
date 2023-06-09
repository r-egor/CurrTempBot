import telebot
import currency_api
import coin_api
import weather_api
from database import DatabaseUsers
from dotenv import load_dotenv
import os

load_dotenv('.env')

bot = telebot.TeleBot(os.getenv('token'))

@bot.message_handler(commands=['start'])
def start(message):
    # Get info about users
    user_id = message.chat.id
    username = message.chat.username
    first_name = message.chat.first_name
    last_name = message.chat.last_name
    language_code = message.from_user.language_code

    # Work with Database users
    database_users = DatabaseUsers()
    # Add&Update user in Database users
    database_users.add_user(user_id, username, first_name, last_name, language_code)

    # User greeting
    greeting = f'Добрый день, {message.from_user.first_name}'
    # Currency rate
    currency_rate = currency_api.CurrencyRate()
    currency = currency_rate.get_currency_rate()
    # Crypto price
    crypto = coin_api.get_crypto_prices()
    # Weather
    weather = weather_api.get_weather_forecast()
    # Send 'start' message
    start_message = f'{greeting}\n\n{currency}\n\n{weather}\n\n{crypto}'
    bot.send_message(message.chat.id, start_message)

@bot.message_handler(commands=['notification_on'])
def push_on(message):
    user_id = message.chat.id
    database = DatabaseUsers()
    database.notification_on_off(user_id, 1)

    notification_on = 'Бот будет присылать уведомления каждый день в 11:00 и 16:00'
    bot.send_message(message.chat.id, notification_on)

@bot.message_handler(commands=['notification_off'])
def push_on(message):
    user_id = message.chat.id
    database = DatabaseUsers()
    database.notification_on_off(user_id, 0)

    notification_on = f'Бот не беспокоит'
    bot.send_message(message.chat.id, notification_on)

bot.polling(none_stop=True)