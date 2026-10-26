FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=18347
    APP_PREFIX=/flask

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 18347

CMD ["gunicorn", "--workers", "1", "--threads", "4", "--bind", "0.0.0.0:18347", "--timeout", "120", "app:app"]
