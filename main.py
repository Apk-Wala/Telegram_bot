from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# --- Your Telegram channel links ---
CHANNEL_LINK_1 = "https://t.me/Apk_wala_official"
CHANNEL_LINK_2 = "https://t.me/Filmycinetime"
# -----------------------------------

# --- Start command handler ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user

    welcome_text = f"""👋 Hello {user.first_name}!
Welcome to our Telegram Bot.

👇 Click the buttons below to join our official channels:"""

    keyboard = [
        [InlineKeyboardButton("📢 Join Apk Wala Official", url=CHANNEL_LINK_1)],
        [InlineKeyboardButton("🎬 Join Filmy Cine Time", url=CHANNEL_LINK_2)]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(welcome_text, reply_markup=reply_markup)

# --- Main function to run the bot ---
def main():
    # 👇 Paste your bot token here
    import os

bot_token = os.getenv("BOT_TOKEN")  # Secure way to load token

app = ApplicationBuilder().token(bot_token).build()
    # Add handlers
    app.add_handler(CommandHandler("start", start))

    print("🤖 Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
