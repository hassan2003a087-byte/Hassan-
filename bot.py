from flask import Flask
from threading import Thread
import telebot

# ==========================================
# 1. كود السيرفر الوهمي لحل مشكلة البورت في Render
# ==========================================
app = Flask('')

@app.route('/')
def home():
    return "Bot is running!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

keep_alive()

# ==========================================
# 2. كود بوت التيليجرام
# ==========================================
# ضع التوكن الخاص بك بين علامتي التنصيص بدلاً من الكلمة
BOT_TOKEN = "8674563347:AAH98OWb9_MiXz4P_1mTu24yLoFkfFi21V8"
bot = telebot.TeleBot(BOT_TOKEN)

# أمر البداية
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "أهلاً بك يا حسن! البوت شغال الآن بنجاح 🚀")

# هنا يمكنك إضافة باقي أوامر البوت الخاصة بك لاحقاً...

# أمر تشغيل البوت باستمرار
bot.infinity_polling()
