from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

from config import BOT_TOKEN, OWNER_ID, CHANNELS


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != OWNER_ID:
        return

    await update.message.reply_text(
        "✅ Daraz Helper Bot Ready!\n\n"
        "📷 ছবি + Caption পাঠাও\n"
        "অথবা শুধু Text পাঠাও।"
    )


async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != OWNER_ID:
        return

    photo = update.message.photo[-1].file_id
    caption = update.message.caption or ""

    success = 0

    for channel in CHANNELS:
        try:
            await context.bot.send_photo(
                chat_id=channel,
                photo=photo,
                caption=caption,
            )
            success += 1
        except Exception as e:
            print(e)

    await update.message.reply_text(
        f"✅ পোস্ট সফল!\n\n{success}/{len(CHANNELS)} টি চ্যানেলে পাঠানো হয়েছে।"
    )


async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != OWNER_ID:
        return

    text = update.message.text

    success = 0

    for channel in CHANNELS:
        try:
            await context.bot.send_message(
                chat_id=channel,
                text=text,
            )
            success += 1
        except Exception as e:
            print(e)

    await update.message.reply_text(
        f"✅ পোস্ট সফল!\n\n{success}/{len(CHANNELS)} টি চ্যানেলে পাঠানো হয়েছে।"
    )


def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.PHOTO, handle_photo))
    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text)
    )

    print("Bot Running...")
    app.run_polling()


if __name__ == "__main__":
    main()
