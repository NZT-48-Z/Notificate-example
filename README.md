# Notificate Microservice

Пример микросервиса для уведомлений о заказах с веб-интерфейсом и Telegram-ботом.

![изображение](https://github.com/user-attachments/assets/d7062ba2-fd5e-43d3-a9a5-1824a01210f0)

![изображение](https://github.com/user-attachments/assets/cc2bc194-c49a-4005-9975-b5f55ea50f8d)

![изображение](https://github.com/user-attachments/assets/f1685485-9d4f-4db5-b954-1e68de9e8884)


## 🚀 Быстрый старт

### Запуск через Docker

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

### Telegram-бот
- Команда `/start` - приветствие
- Команда `/id` - получение chat_id
- Уведомления о заказах

### API
- `GET /` - веб-интерфейс
- `GET /health` - проверка здоровья сервиса
- `POST /order?name=...` - создание заказа

## 🐳 Docker

- **API**: порт 8000
- **RabbitMQ**: порт 5672 (AMQP), 15672 (веб-интерфейс)
- **Бот**: работает в фоне

## 📁 Структура проекта

```
notificate/
├── .git/
├── .pytest_cache/
├── .mypy_cache/
├── .venv/
├── src/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── config.py
│   │   ├── static/
│   │   │   └── index.html
│   │   ├── api/
│   │   │   ├── __init__.py
│   │   │   └── order.py
│   │   └── __pycache__/
│   ├── broker/
│   │   ├── __init__.py
│   │   ├── rabbit.py
│   │   └── __pycache__/
│   └── bot_worker/
│       ├── __init__.py
│       ├── main.py
│       ├── config.py
│       ├── Dockerfile
│       └── __pycache__/
├── pyproject.toml
├── uv.lock
├── Dockerfile
├── Dockerfile.bot
├── docker-compose.yaml
├── .gitignore
├── .python-version
└── README.md
```

## 🔧 Переменные окружения

- `RABBIT_URL` — строка подключения к RabbitMQ
- `BOT_TOKEN` — токен Telegram-бота
- `ADMIN_CHAT_ID` — chat_id администратора

## 📊 Мониторинг

- Healthcheck: `GET /health`
- RabbitMQ Management: http://localhost:15672 (guest/guest)
- API документация: http://localhost:8000/docs 
