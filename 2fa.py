import telebot
import pyotp

Tiger = '6918566731:AAFisBJbgYzRfhU7M6LVp6dZNazxfZGadYY'  # Ganti dengan token bot Telegram Anda
bot = telebot.TeleBot(Tiger)

def generate_otp(secret_key):
    totp = pyotp.TOTP(secret_key)
    return totp.now()

def is_valid_secret_key(secret_key):
    return len(secret_key) >= 16

@bot.message_handler(commands=['start'])
def send_otp(message):
    bot.reply_to(message, "Silakan masukkan secret key untuk menghasilkan OTP:")

@bot.message_handler(func=lambda message: True)
def process_secret_key(message):
    secret_key = message.text.strip().replace(" ", "")
    if not is_valid_secret_key(secret_key):
        bot.reply_to(message, "Kunci rahasia harus memiliki minimal 16 digit.")
    else:
        try:
            otp = generate_otp(secret_key)
            bot.reply_to(message, f"🔒 Kode OTP Anda:\n\n{otp}\n\n✨ Silakan salin (copy) kode di atas untuk digunakan.")
        except Exception as e:
            bot.reply_to(message, "Terjadi kesalahan dalam menghasilkan OTP. Mohon coba lagi.")

print("Bot berjalan...")
bot.polling(none_stop=True)
