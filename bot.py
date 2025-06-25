import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# ✅ Securely store token as environment variable (best practice for Render)
import os
TOKEN = os.environ.get("BOT_TOKEN")  # Replace with your token directly for local testing if needed

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
    await update.message.reply_text(
        "🆘 Help Commands:\n"
        "/start - Bot shuru karo\n"
        "/help - Madad lo\n"
        "/about - Bot ke baare mein"
    )

# /about command
async def about_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Main ek Vedic Astrology chatbot hoon, banaya gaya Devendra Agrawal ke dwara 🔮")

# Main application runner
def main():
    if not TOKEN:
        raise ValueError("BOT_TOKEN environment variable not set!")

    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("about", about_command))
    app.run_polling()

if __name__ == "__main__":
    main()
