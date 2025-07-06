FROM python:3.12-slim
WORKDIR /app
RUN pip install --no-cache-dir fastapi aio-pika aiogram python-dotenv aiofiles uvicorn
# Копируем весь проект
COPY . .
# Копируем модули из родительских папок
COPY ../broker ./broker
COPY ../app ./app
CMD ["python", "main.py"] 