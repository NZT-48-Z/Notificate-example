import os

RABBIT_URL = os.getenv("RABBIT_URL", "amqp://guest:guest@localhost/")
BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_CHAT_ID = os.getenv("ADMIN_CHAT_ID")
