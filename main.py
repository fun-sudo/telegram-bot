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
