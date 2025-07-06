from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.api.order import router as order_router
from broker.rabbit import broker
import asyncio

from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app):
    """Lifespan-менеджер для подключения и отключения брокера"""
    max_retries = 30
    retry_delay = 2

    for attempt in range(max_retries):
        try:
            await broker.connect()
            print("Брокер RabbitMQ подключен")
            break
        except Exception as e:
            print(
                f"Попытка {attempt + 1}/{max_retries} подключения к RabbitMQ: {e}")
            if attempt < max_retries - 1:
                await asyncio.sleep(retry_delay)
            else:
                print("Не удалось подключиться к RabbitMQ после всех попыток")
                raise

    yield

    await broker.close()
    print("Брокер RabbitMQ отключен")

app = FastAPI(title="Notificate API", version="1.0.0", lifespan=lifespan)

app.mount("/static", StaticFiles(directory="app/static"), name="static")
app.include_router(order_router)
