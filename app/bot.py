import logging

from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
)

from .config import load_settings
from .handlers import start, help_command, chat_id, message_handler

def main() -> None:
    settings = load_settings()

    logging.basicConfig(
        level=getattr(logging, settings.log_level, logging.INFO),
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    )

    app = Application.builder().token(settings.bot_token).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("id", chat_id))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message_handler))

    logging.info("Telegram bot starting...")
    app.run_polling(allowed_updates=["message"])

if __name__ == "__main__":
    main()
