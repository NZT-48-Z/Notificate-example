from broker.rabbit import broker
from config import BOT_TOKEN, ADMIN_CHAT_ID
from aiogram.filters import Command
from aiogram.types import Message
from aiogram import Bot, Dispatcher
import asyncio
import logging
import sys
import os
from pathlib import Path

from dotenv import load_dotenv

# Загружаем переменные окружения из .env файла
env_path = Path(__file__).parent.parent.parent / '.env'
load_dotenv(env_path)


dp = Dispatcher()

if not BOT_TOKEN:
    raise RuntimeError("Переменная окружения BOT_TOKEN не задана!")

bot = Bot(token=BOT_TOKEN)


@dp.message(Command("start"))
async def cmd_start(message: Message):
    user_id = message.from_user.id if message.from_user else "Неизвестный пользователь"
    logging.info(f"/start от {user_id}")
    await message.answer("Привет! Я бот для уведомлений о заказах.")


@dp.message(Command("id"))
async def cmd_id(message: Message):
    user_id = message.from_user.id if message.from_user else "Неизвестный пользователь"
    logging.info(f"/id от {user_id}")
    await message.answer(f"Ваш chat_id: {message.chat.id}")


@dp.message()
async def unknown_command(message: Message):
    user_id = message.from_user.id if message.from_user else "Неизвестный пользователь"
    logging.info(f"Неизвестная команда от {user_id}: {message.text}")
    await message.answer("Неизвестная команда. Доступно: /start, /id")


async def handle_orders_and_send_message(message):
    """Обработчик сообщений из очереди orders"""
    async with message.process():
        try:
            data = message.body.decode()
            if ADMIN_CHAT_ID:
                await bot.send_message(chat_id=ADMIN_CHAT_ID, text=data)
                logging.info(f"Уведомление отправлено: {data}")
            else:
                logging.error("ADMIN_CHAT_ID не задан!")
        except Exception as e:
            logging.error(f"Ошибка при отправке сообщения: {e}")


async def main():
    # Подключаемся к RabbitMQ
    await broker.connect()
    logging.info("Брокер подключен")

    # Проверяем, что канал создан
    if not broker.channel:
        raise RuntimeError("Канал не инициализирован")

    # Объявляем очередь и начинаем слушать
    queue = await broker.channel.declare_queue("orders", durable=True)

    # Запускаем обработку сообщений
    await queue.consume(handle_orders_and_send_message)
    logging.info("Начинаем слушать очередь orders")

    # Запускаем бота
    await dp.start_polling(bot)

    # Закрываем подключение
    await broker.close()
    logging.info("Все закончилось...")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
