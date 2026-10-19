FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV SECRET_KEY=solo-para-build
ENV DEBUG=False

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Archivos estaticos
RUN python manage.py collectstatic --no-input

# Base de datos lista con el catalogo cargado
RUN python manage.py migrate --no-input
RUN python manage.py loaddata datos.json

EXPOSE 8000

CMD ["sh", "-c", "gunicorn musicpro.wsgi:application --bind 0.0.0.0:${PORT:-8000} --workers 2 --timeout 120"]
