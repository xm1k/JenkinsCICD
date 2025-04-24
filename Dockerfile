FROM python:3.9-slim
WORKDIR /app

# Копируем зависимости
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Копируем всё приложение
COPY . .

EXPOSE 5000

# Отключаем reloader, чтобы контейнер не падал
CMD ["python", "app.py", "--host=0.0.0.0", "--port=5000", "--no-reload"]

