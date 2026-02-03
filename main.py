import telebot

# BotFather se mila token yahan ' ' ke beech dalein
API_TOKEN = '8266839607:AAF0WfXeW1-A93UrQyD7oIquN7FHZLsXlRM'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Hello! I'm Anna.")

@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message, "How may I help you?")

# Bot ko chalu rakhne ke liye
bot.infinity_polling()
import telebot
from flask import Flask
from threading import Thread

# 1. Web Server Setup (Flask)
app = Flask('')

@app.route('/')
def home():
    return "Bot is Alive!"

def run():
  app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

# 2. Bot Setup
API_TOKEN = '8266839607:AAF0WfXeW1-A93UrQyD7oIquN7FHZLsXlRM'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Main hamesha active hoon!")

# 3. Dono ko saath chalana
if __name__ == "__main__":
    keep_alive()  # Server shuru karega
    bot.infinity_polling() # Bot shuru karega
