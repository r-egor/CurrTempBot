import telebot
import currency_api
import coin_api
import weather_api
import settings_bot
from database import DatabaseUsers
import schedule
import time

bot = telebot.TeleBot(settings_bot.token)

def send_daily_message():
    database_users = DatabaseUsers()
    users = database_users.get_user()
    for user in users:
        try:
            # User greeting
            greeting = f'Добрый день, {user[1]}'
            # Currency rate
            currency = currency_api.get_currency_rate()
            # Crypto price
            crypto = coin_api.get_crypto_prices()
            # Weather
            weather = weather_api.get_weather_forecast()
            # Send daily message
            daily_message = f"{greeting}\n\n{currency}\n\n{weather}\n\n{crypto}"
            bot.send_message(user[0], daily_message)
        except telebot.apihelper.ApiTelegramException as error:
            # If the user has blocked the bot, delete the user from the database
            if error.result.status_code == 403:
                database_users.delete_user(user[0])

# Schedule the daily message to be sent every day at 11:00 and 16:00
schedule.every().day.at("11:00").do(send_daily_message)
schedule.every().day.at("16:00").do(send_daily_message)

# Run the schedule loop
while True:
    schedule.run_pending()
    time.sleep(1)
