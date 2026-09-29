from telegram import Update
from telegram.ext import ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Bot aktif. Kirim pesan atau gunakan /help."
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Command tersedia:\n"
        "/start - mulai bot\n"
        "/help - bantuan\n"
        "/id - tampilkan Chat ID"
    )

async def chat_id(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f"Chat ID: {update.effective_chat.id}")

async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not update.message or not update.message.text:
        return
    await update.message.reply_text(f"Anda: {update.message.text}")
