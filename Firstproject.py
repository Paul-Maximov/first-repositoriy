import telebot
import random
from config import TOKEN
from bot_logic import gen_pass

    # Замени 'TOKEN' на токен твоего бота
    # Этот токен ты получаешь от BotFather, чтобы бот мог работать
bot = telebot.TeleBot(TOKEN)
games = ["roblox", "cs2", "dota", "brawl stars"]
coin = ["орел", "решка"]

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "привет! я бот и могу принять сообщение")

@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Как дела?")

@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")

@bot.message_handler(commands=["password"])
def send_return(message):
    bot.reply_to(message, gen_pass(10))

@bot.message_handler(commands=["coin"])
def send_coin(message):
    bot.reply_to(message, random.choice(coin))


@bot.message_handler(commands=['games'])
def send_games(message):
    bot.reply_to(message, random.choice(games))

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.polling()
