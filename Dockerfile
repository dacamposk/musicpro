FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Genera los archivos estaticos dentro de la imagen
RUN SECRET_KEY=solo-para-build DEBUG=False python manage.py collectstatic --no-input

EXPOSE 8000

# Aplica migraciones y levanta el servidor de produccion
CMD ["sh", "-c", "python manage.py migrate --no-input && gunicorn musicpro.wsgi:application --bind 0.0.0.0:${PORT:-8000} --workers 2 --timeout 120"]
