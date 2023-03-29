import telebot
from bot_token import token


bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    # User greeting
    greeting = f'Добрый день, {message.from_user.first_name}'
    bot.send_message(message.chat.id, greeting)

bot.polling(none_stop=True)
