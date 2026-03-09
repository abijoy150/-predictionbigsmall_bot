import telebot
import random

TOKEN = "8635867898:AAHsg3EuEASb60qZuSFqpB2GzU6GpwyE_T8"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Send result like: B S S B")

@bot.message_handler(func=lambda m: True)
def predict(message):
    prediction = random.choice(["BIG","SMALL"])
    bot.reply_to(message, "Next Prediction: " + prediction)

bot.infinity_polling()
