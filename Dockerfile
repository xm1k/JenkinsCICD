# Используем официальный образ Python 3.9 slim
FROM python:3.9-slim

# Рабочая директория внутри контейнера
WORKDIR /app

# Копируем зависимости и устанавливаем их
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем все остальные файлы приложения
COPY . .

# Открываем порт, на котором будет слушать Flask
EXPOSE 5000

# Отключаем встроенный reloader и debug-модуль в Flask,
# чтобы в контейнере был только один процесс и он не завершался сразу.
CMD ["python", "app.py", "--host=0.0.0.0", "--port=5000", "--no-reload"]

