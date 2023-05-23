import telebot
import currency_api
import coin_api
import weather_api
from database import DatabaseUsers
import schedule
import time
from dotenv import load_dotenv
import os

load_dotenv('.env')

bot = telebot.TeleBot(os.getenv('token'))

def get_info():
    # Currency rate
    currency_rate = currency_api.CurrencyRate()
    currency = currency_rate.get_currency_rate()
    # Crypto price
    crypto = coin_api.get_crypto_prices()
    # Weather
    weather = weather_api.get_weather_forecast()
    # All info into one variable
    daily_info = f"{currency}\n\n{weather}\n\n{crypto}"
    return daily_info

def send_daily_message():
    database_users = DatabaseUsers()
    # Get daily information
    daily_info = get_info()
    users = database_users.get_user()
    for user in users:
        try:
            # User greeting
            greeting = f'Добрый день, {user[1]}'
            # Get daily information
            daily_info = get_info()
            # Send daily message
            daily_message = f"{greeting}\n\n{daily_info}"
            bot.send_message(user[0], daily_message)
        except telebot.apihelper.ApiTelegramException as error:
            # If the user has blocked the bot, delete the user from the database
            if error.result.status_code == 403:
                database_users.delete_user(user[0])

def scheduler_get_currency_for_database():
    currency_rate = currency_api.CurrencyRate()
    currency_rate.get_currency_for_database()

# Schedule for get currency rate and save to database
schedule.every().day.at("10:00").do(scheduler_get_currency_for_database)

# Schedule the daily message to be sent every day at 11:00
schedule.every().day.at("14:10").do(send_daily_message)
schedule.every().day.at("16:00").do(send_daily_message)

# Run the schedule loop
while True:
    schedule.run_pending()
    time.sleep(1)
