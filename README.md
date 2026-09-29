# Telegram Bot — boot

Template Telegram Bot siap pakai untuk project multi-agent/API.

## Fitur
- Telegram Bot API via python-telegram-bot
- Konfigurasi melalui .env
- Command /start, /help, /id
- Echo pesan
- Struktur siap ditambah multi-agent dan API
- Token tidak disimpan di repository

## Setup Windows PowerShell

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy-Item .env.example .env
notepad .env
python -m app.bot
```

Isi .env:

```env
BOT_TOKEN=123456:YOUR_BOT_TOKEN
CHAT_ID=
```

BOT_TOKEN berasal dari BotFather. Jangan commit file .env.

## Command
- /start
- /help
- /id

Setelah bot hidup, kirim pesan ke bot lalu gunakan /id untuk mengetahui chat ID.
