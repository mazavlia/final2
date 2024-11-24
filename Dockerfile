FROM python:3.10-slim

WORKDIR /app

# Копируйте requirements.txt и устанавливайте зависимости
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Копируйте все файлы в рабочую директорию
COPY . .

# Запустите main.py
CMD ["python", "main.py"]

