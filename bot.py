import telebot

TOKEN = '8674563347:AAH98OWb9_MiXz4P_1mTu24yLoFkfFi21V8'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "أهلاً يا حسن! البوت جاهز، أرسل كلمة: إشارة")

@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    if "إشارة" in message.text:
        bot.send_message(message.chat.id, "🚨 إشارة تداول جديدة (Quotex)\n📈 الزوج: EUR/USD\n🟢 التوقع: صعود (Call)\n⏰ المدة: 1 دقيقة")
    else:
        bot.send_message(message.chat.id, "وصلت رسالتك. أرسل كلمة (إشارة) فقط ليعطيك الصفقة.")

bot.infinity_polling()
