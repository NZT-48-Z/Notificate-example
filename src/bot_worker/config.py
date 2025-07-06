import os

BOT_TOKEN = os.getenv('BOT_TOKEN')
ADMIN_CHAT_ID = int(os.getenv('ADMIN_CHAT_ID', '0')
                    ) if os.getenv('ADMIN_CHAT_ID') else None
RABBIT_URL = os.getenv('RABBIT_URL', 'amqp://guest:guest@localhost/')
