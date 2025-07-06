# Notificate Microservice

Современный микросервис для уведомлений о заказах с веб-интерфейсом и Telegram-ботом.

## 🚀 Быстрый старт

### Запуск через Docker (рекомендуется)

1. Создайте файл `.env` в корне проекта:
```env
RABBIT_URL=amqp://guest:guest@localhost/
BOT_TOKEN=ВАШ_ТОКЕН_БОТА
ADMIN_CHAT_ID=ВАШ_CHAT_ID
```

2. Запустите все сервисы:
```bash
docker-compose up --build
```

3. Откройте веб-интерфейс: http://localhost:8000

### Запуск локально

1. Установите зависимости:
```bash
pip install -r requirements.txt
```

2. Запустите FastAPI:
```bash
uvicorn app.main:app --reload
```

3. Запустите воркер (бота):
```bash
python bot_worker/main.py
```

## 📋 Функциональность

### Веб-интерфейс
- Современный дизайн с градиентами и анимациями
- Форма создания заказов
- Индикатор загрузки
- Проверка статуса сервисов
- Адаптивный дизайн

### Telegram-бот
- Команда `/start` - приветствие
- Команда `/id` - получение chat_id
- Автоматические уведомления о заказах
- Обработка ошибок и логирование

### API
- `GET /` - веб-интерфейс
- `GET /health` - проверка здоровья сервиса
- `POST /order?name=...` - создание заказа

## 🧪 Тестирование

```bash
pytest
```

## 🐳 Docker

- **API**: порт 8000
- **RabbitMQ**: порт 5672 (AMQP), 15672 (веб-интерфейс)
- **Бот**: работает в фоне

## 📁 Структура проекта

```
notificate/
├── app/
│   ├── api/          # FastAPI роуты
│   ├── broker/       # RabbitMQ брокер
│   ├── static/       # HTML/CSS/JS файлы
│   ├── config.py     # Конфигурация
│   └── main.py       # Точка входа FastAPI
├── bot_worker/       # Telegram-бот
├── tests/           # Тесты
├── docker-compose.yaml
└── requirements.txt
```

## 🔧 Переменные окружения

- `RABBIT_URL` — строка подключения к RabbitMQ
- `BOT_TOKEN` — токен Telegram-бота
- `ADMIN_CHAT_ID` — chat_id администратора

## 📊 Мониторинг

- Healthcheck: `GET /health`
- RabbitMQ Management: http://localhost:15672 (guest/guest)
- API документация: http://localhost:8000/docs 