from telegram.ext import Updater
from app.config import config
from app.handlers import register_handlers


def run_bot():
    updater = Updater(token=config.BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    # handlerlarni ulash
    register_handlers(dp)
    

    print("🤖 Bot ishga tushdi...")
    updater.start_polling()
    updater.idle()
