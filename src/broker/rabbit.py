import os
import aio_pika
from aio_pika import connect_robust, Message
from app.config import RABBIT_URL


class RabbitBroker:
    def __init__(self, url: str):
        self.url = url
        self.connection = None
        self.channel = None

    async def connect(self):
        """Подключение к RabbitMQ"""
        self.connection = await connect_robust(self.url)
        self.channel = await self.connection.channel()
        print("Подключение к RabbitMQ установлено")

    async def close(self):
        """Закрытие подключения к RabbitMQ"""
        if self.connection:
            await self.connection.close()
            print("Подключение к RabbitMQ закрыто")

    async def publish_order(self, message: str):
        """Публикация сообщения в очередь orders"""
        if not self.channel:
            raise RuntimeError(
                "Канал не инициализирован. Вызовите connect() сначала")

        # Объявляем очередь, если она не существует
        queue = await self.channel.declare_queue("orders", durable=True)

        # Создаем сообщение
        message_obj = Message(
            body=message.encode(),
            delivery_mode=aio_pika.DeliveryMode.PERSISTENT
        )

        # Публикуем сообщение
        await self.channel.default_exchange.publish(
            message_obj,
            routing_key="orders"
        )
        print(f"Сообщение отправлено в очередь orders: {message}")


# Создаем экземпляр брокера
broker = RabbitBroker(RABBIT_URL)
