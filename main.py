import telebot
from api import coin_api, weather_api, currency_api
from telebot import types
from services.database import DatabaseUsers
from services.currency_converter import Curr_converter
from dotenv import load_dotenv
import os

load_dotenv('.env')

bot = telebot.TeleBot(os.getenv('token'))

weather_obj = weather_api.Weather_forecast()


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
    weather = weather_obj.get_weather('main')
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
def push_off(message):
    user_id = message.chat.id
    database = DatabaseUsers()
    database.notification_on_off(user_id, 0)

    notification_off = f'Бот не беспокоит'
    bot.send_message(message.chat.id, notification_off)


@bot.message_handler(commands=['convert'])
def show_currency_menu(message):
    # Display menu buttons
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=4)
    usd_button = types.KeyboardButton('USD')
    eur_button = types.KeyboardButton('EUR')
    rub_button = types.KeyboardButton('RUB')
    byn_button = types.KeyboardButton('BYN')

    markup.add(usd_button, eur_button, rub_button, byn_button)
    bot.send_message(message.chat.id, 'Выберите начальную валюту для конвертации:', reply_markup=markup)
    # Save the current state of the user (waiting for the source currency selection)
    bot.register_next_step_handler(message, select_destination_currency)


def select_destination_currency(message):
    # Save the selected source currency in the user's state
    source_currency = message.text

    # Display menu buttons for selecting the destination currency
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=4)
    usd_button = types.KeyboardButton('USD')
    eur_button = types.KeyboardButton('EUR')
    rub_button = types.KeyboardButton('RUB')
    byn_button = types.KeyboardButton('BYN')
    markup.add(usd_button, eur_button, rub_button, byn_button)
    bot.send_message(message.chat.id, 'Выберите валюту, в которую нужно сконвертировать:', reply_markup=markup)
    # Save the selected source currency in the user's state
    # Register a new step handler to wait for the destination currency selection
    bot.register_next_step_handler(message, select_amount, source_currency)


def select_amount(message, source_currency):
    try:
        # Save the selected destination currency in the user's state
        destination_currency = message.text

        # Ask the user for the amount to convert
        bot.send_message(message.chat.id, "Введите сумму для конвертации:")
        # Save the selected destination currency in the user's state
        # Register a new step handler to wait for the amount input
        bot.register_next_step_handler(message, perform_conversion, source_currency, destination_currency)
    except Exception as e:
        bot.send_message(message.chat.id, str(e))


def perform_conversion(message, source_currency, destination_currency):
    try:
        amount = float(message.text)
        # Method from the Curr_converter object
        converter = Curr_converter()
        converted_amount = converter.convert(amount, source_currency, destination_currency)
        # Displaying the result
        bot.send_message(message.chat.id, f"{amount} {source_currency} = {converted_amount} {destination_currency}")
    except ValueError:
        bot.send_message(message.chat.id, "Неверное значение суммы для конвертации.")
    except Exception as e:
        bot.send_message(message.chat.id, str(e))


@bot.message_handler(commands=['regional_weather'])
def show_regional_weather_menu(message):
    # Display menu buttons
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    brest_reg = types.KeyboardButton('Brest region')
    vitebsk_reg = types.KeyboardButton('Vitebsk region')
    gomel_reg = types.KeyboardButton('Gomel region')
    grodno_reg = types.KeyboardButton('Grodno region')
    minsk_reg = types.KeyboardButton('Minsk region')
    mogilev_reg = types.KeyboardButton('Mogilev region')

    markup.add(brest_reg, vitebsk_reg, grodno_reg, gomel_reg, minsk_reg, mogilev_reg)

    # Send the menu message
    bot.send_message(message.chat.id, 'Выберите регион:', reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == 'Brest region')
def get_weather_brest_reg(message):
    brest_reg_weather_data = weather_obj.get_weather('brest')
    bot.send_message(message.chat.id, brest_reg_weather_data)


@bot.message_handler(func=lambda message: message.text == 'Vitebsk region')
def get_weather_vetbsk_reg(message):
    vitebsk_reg_weather_data = weather_obj.get_weather('vitebsk')
    bot.send_message(message.chat.id, vitebsk_reg_weather_data)


@bot.message_handler(func=lambda message: message.text == 'Gomel region')
def get_weather_gomel_reg(message):
    gomel_reg_weather_data = weather_obj.get_weather('gomel')
    bot.send_message(message.chat.id, gomel_reg_weather_data)


@bot.message_handler(func=lambda message: message.text == 'Grodno region')
def get_weather_grodno_reg(message):
    grodno_reg_weather_data = weather_obj.get_weather('grodno')
    bot.send_message(message.chat.id, grodno_reg_weather_data)


@bot.message_handler(func=lambda message: message.text == 'Minsk region')
def get_weather_minsk_reg(message):
    minsk_reg_weather_data = weather_obj.get_weather('minsk')
    bot.send_message(message.chat.id, minsk_reg_weather_data)


@bot.message_handler(func=lambda message: message.text == 'Mogilev region')
def get_weather_mogilev_reg(message):
    mogilev_reg_weather_data = weather_obj.get_weather('mogilev')
    bot.send_message(message.chat.id, mogilev_reg_weather_data)


bot.polling(none_stop=True)
