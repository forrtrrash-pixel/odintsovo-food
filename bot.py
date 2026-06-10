from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = 8805486704:AAFDBv-pJuUs89EM3baQjNKF3MNzjM7vUyA
ADMIN_ID = 414499892  # ВСТАВЬ СВОЙ TELEGRAM ID


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🥣 Окрошка на квасе", callback_data="Окрошка на квасе")],
        [InlineKeyboardButton("🥣 Окрошка на кефире", callback_data="Окрошка на кефире")],
        [InlineKeyboardButton("🔥 Люля", callback_data="Люля")],
        [InlineKeyboardButton("🍗 Курица", callback_data="Курица")],
        [InlineKeyboardButton("🥬 Овощи (мангал)", callback_data="Овощи (мангал)")],
        [InlineKeyboardButton("🥗 Салат Цезарь", callback_data="Салат Цезарь")],
        [InlineKeyboardButton("🐟 Нарезка рыбная", callback_data="Нарезка рыбная")],
        [InlineKeyboardButton("🍅 Овощи", callback_data="Овощи")],
        [InlineKeyboardButton("🧀 Нарезка сырная", callback_data="Нарезка сырная")],
        [InlineKeyboardButton("🥩 Нарезка мясная", callback_data="Нарезка мясная")],
    ]

    await update.message.reply_text(
        "Выберите блюдо:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    user = query.from_user
    food = query.data

    await query.edit_message_text(
        f"✅ Ваш выбор: {food}"
    )

    await context.bot.send_message(
        chat_id=ADMIN_ID,
        text=(
            f"🔔 Новый заказ\n\n"
            f"👤 Имя: {user.full_name}\n"
            f"🆔 ID: {user.id}\n"
            f"🍽 Блюдо: {food}"
        )
    )


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))

    print("Бот запущен")
    app.run_polling()


if __name__ == "__main__":
    main()
