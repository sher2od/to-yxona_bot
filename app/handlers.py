from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from telegram.ext import (
    CommandHandler, CallbackContext, MessageHandler,
    Filters, ConversationHandler
)

from .services import save_user  # faqat chaqiramiz


# States
ASK_NAME, ASK_CONTACT, ASK_DATE, ASK_GUESTS, CONFIRM = range(5)

# /start
def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Assalomu alaykum!\n\n"
        "Bu bot orqali to‘yxona band qilishingiz mumkin 🎉\n\n"
        "Ro'yxatdan o'tish uchun tugmani bosing 👇",
        reply_markup=ReplyKeyboardMarkup(
            [[KeyboardButton("Ro'yxatdan o'tish")]],
            resize_keyboard=True
        )
    )

# 1 - ism
def register_start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Ismingizni kiriting:",
        reply_markup=ReplyKeyboardRemove()
        )
    return ASK_NAME

def ask_name(update: Update, context: CallbackContext):
    context.user_data["name"] = update.message.text
    update.message.reply_text(
        "📞 Telefon raqamingizni yuboring:",
        reply_markup=ReplyKeyboardMarkup(
            [[KeyboardButton("📞 Raqamni yuborish", request_contact=True)]],  
            resize_keyboard=True,
            one_time_keyboard=True
        )
    )
    return ASK_CONTACT

# 2-contact
def ask_contact(update: Update, context: CallbackContext):
    contact = update.message.contact.phone_number
    context.user_data["contact"] = contact  

    update.message.reply_text(
        "📅 To‘y sanasini kiriting (masalan: 2025-09-15):",
        reply_markup=ReplyKeyboardRemove()
    )
    return ASK_DATE

# 3 - sanani olish
def ask_date(update: Update, context: CallbackContext):
    context.user_data["date"] = update.message.text
    update.message.reply_text("👥 Mehmonlar sonini kiriting:")
    return ASK_GUESTS

# 4 - mehmonlar soni
def ask_guests(update: Update, context: CallbackContext):
    context.user_data["guests"] = update.message.text

    name = context.user_data["name"]
    contact = context.user_data["contact"]
    date = context.user_data["date"]
    guests = context.user_data["guests"]

    update.message.reply_text(
        f"✅ Ma’lumotlaringiz:\n\n"
        f"👤 Ism: {name}\n"
        f"📞 Raqam: {contact}\n"
        f"📅 Sana: {date}\n"
        f"👥 Mehmonlar soni: {guests}\n\n"
        f"Tasdiqlaysizmi?",
        reply_markup=ReplyKeyboardMarkup(
            [["✅ Tasdiqlash", "✏️ Tahrirlash"]],
            resize_keyboard=True
        )
    )
    return CONFIRM


# 5 - tasdiqlash
def confirm(update: Update, context: CallbackContext):
    if update.message.text == "✅ Tasdiqlash":
        # bazaga yozamiz
        save_user(context.user_data, update.effective_user.id)

        update.message.reply_text(
            "🎉 Ma’lumotlaringiz saqlandi! Rahmat.",
            reply_markup=ReplyKeyboardRemove()
        )
        context.user_data.clear()
        return ConversationHandler.END
    else:
        update.message.reply_text(
            "Qaysi joyni tahrirlashni xohlaysiz?\n"
            "👉 Hozircha qaytadan boshlash uchun /start bosing."
        )
        return ConversationHandler.END


# Handlerlar
def register_handlers(dp):
    conv_handler = ConversationHandler(
        entry_points=[MessageHandler(Filters.regex("Ro'yxatdan o'tish"), register_start)],
        states={
            ASK_NAME: [MessageHandler(Filters.text & ~Filters.command, ask_name)],
            ASK_CONTACT: [MessageHandler(Filters.contact, ask_contact)],
            ASK_DATE: [MessageHandler(Filters.text & ~Filters.command, ask_date)],
            ASK_GUESTS: [MessageHandler(Filters.text & ~Filters.command, ask_guests)],
            CONFIRM: [MessageHandler(Filters.regex("^(✅ Tasdiqlash|✏️ Tahrirlash)$"), confirm)],
        },
        fallbacks=[]
    )

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(conv_handler)
