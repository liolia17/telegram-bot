from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

menu = [["📅 Запись", "🕒 Расписание"], ["📍 Адрес", "📞 Телефоны"]]

async def start(update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Здравствуйте! Я бот клиники. Чем могу помочь?",
        reply_markup=ReplyKeyboardMarkup(menu, resize_keyboard=True)
    )

async def handle_message(update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "📅 Запись":
        await update.message.reply_text("Позвоните координатору: +7 999 123 4567")
    elif text == "🕒 Расписание":
        await update.message.reply_text("Пн-Сб: 9:00–18:00\nВс: выходной")
    elif text == "📍 Адрес":
        await update.message.reply_text("г. Москва, ул. Примерная, д. 1")
    elif text == "📞 Телефоны":
        await update.message.reply_text("Координатор: +7 999 123 4567\nРесепшн: +7 999 765 4321")
    else:
        await update.message.reply_text("Пожалуйста, выберите вариант из меню.")

app = ApplicationBuilder().token("8032522838:AAEbjmbvXRXUj9DlyTL_y3AEid1DnlA5I9c").build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

app.run_polling()
