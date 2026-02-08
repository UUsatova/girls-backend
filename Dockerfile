# girls-backend/Dockerfile
FROM python:3.12-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt gunicorn

COPY . /app/

EXPOSE 8000

CMD ["gunicorn", "girls_backend.wsgi:application", "--bind", "0.0.0.0:8000"]
