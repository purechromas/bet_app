FROM python:3.10

LABEL creator="Blagovest Krasimirov Nedkov"
LABEL tags="PYTHON | FASTAPI | SQLALCHEMY | POSTGRESQL | RABBITMQ | REDIS | ASYNCIO"
LABEL version="1.0"

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PIP_NO_CACHE_DIR=off


WORKDIR /bet_app

RUN apt-get update && apt-get install -y --no-install-recommends libpq-dev gcc \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
RUN python3 setup.py develop

