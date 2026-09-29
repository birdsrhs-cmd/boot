import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()

@dataclass(frozen=True)
class Settings:
    bot_token: str
    chat_id: str | None
    api_base_url: str | None
    api_key: str | None
    log_level: str

def load_settings() -> Settings:
    token = os.getenv("BOT_TOKEN", "").strip()
    if not token:
        raise RuntimeError("BOT_TOKEN belum diisi. Isi file .env terlebih dahulu.")

    chat_id = os.getenv("CHAT_ID", "").strip() or None
    return Settings(
        bot_token=token,
        chat_id=chat_id,
        api_base_url=os.getenv("API_BASE_URL", "").strip() or None,
        api_key=os.getenv("API_KEY", "").strip() or None,
        log_level=os.getenv("LOG_LEVEL", "INFO").strip().upper(),
    )
