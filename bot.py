import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Replace this with your actual token
TOKEN = "7392937646:AAHnaXYgAQVQeqVh5AcJCKslvVWKuy9ku5s"

# Logging setup
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("🙏 Jai Shree Ram, Devendra Astro ChatBot mein aapka swagat hai!")

# /help command
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Help Command: Yeh bot astrology related sawalon ke jawab deta hai. /start se shuru karein.")
/start - Shuru karo
/help - Madad lo")

# Main application runner
def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.run_polling()

if __name__ == "__main__":
    main()
