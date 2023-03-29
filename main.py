import telebot
import nbrb_api
from bot_token import token


bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    # User greeting
    greeting = f'Добрый день, {message.from_user.first_name}'
    # Currency rate for User
    usd = nbrb_api.get_currency_rate()
    # Send 'start' message
    start_message = f'{greeting}\n\n{usd}'
    bot.send_message(message.chat.id, start_message)


bot.polling(none_stop=True)
