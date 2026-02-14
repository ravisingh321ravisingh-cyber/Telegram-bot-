import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

TOKEN = os.environ.get("8339736684:AAEyZsxweGT4ebToh3ThG6gfqopUzfjM4og")

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Bot working successfully!")

updater = Updater(TOKEN)
dp = updater.dispatcher
dp.add_handler(CommandHandler("start", start))

updater.start_polling()
updater.idle()
