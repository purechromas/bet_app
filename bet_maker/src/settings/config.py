import os

from pathlib import Path
from dataclasses import dataclass


@dataclass(frozen=True)
class Config:
    # БЕЗ ПЕРЕМЕННЫХ ОКРУЖЕНИЯ 🔴
    BASE_DIR = Path(__file__).resolve().parent.parent.parent
    DEBUG = bool(os.environ.get("DEBUG", True))

    APP_NAME = "bet_maker"
    APP_HOST = str(os.environ.get("APP_HOST", "localhost"))
    APP_PORT = int(os.environ.get("APP_PORT", 8001))

    CONSOLE_LOG_LEVEL = str(os.environ.get("CONSOLE_LOG_LEVEL", "DEBUG"))
    FILE_LOG_LEVEL = str(os.environ.get("FILE_LOG_LEVEL", "ERROR"))

    # POSTGRES DB
    PG_URL = str(os.environ.get("PG_URL", "postgresql+asyncpg://qwe123:qwe123@localhost:5432/bet_maker"))
    PG_POOL_SIZE = int(os.environ.get("PG_POOL_SIZE", 10))
    PG_POOL_TIMEOUT = int(os.environ.get("PG_POOL_TIMEOUT", 60))

    # ORM
    SQLALCHEMY_ECHO = bool(os.environ.get("SQLALCHEMY_ECHO", 0))

    # LINE PROVIDER SERVICE
    LINE_PROVIDER_GRPC_SERVER_URL = str(os.environ.get("LINE_PROVIDER_GRPC_SERVER_URL", "localhost:50051"))

    # RABBITMQ MESSAGE BROKER
    AMQP_URL = str(os.environ.get("AMQP_URL", "amqp://admin:admin@localhost:5672"))
    AMQP_ROUTING_KEY_LOGGER = str(os.environ.get("AMQP_ROUTING_KEY_LOGGER", "logstash"))

    # REDIS CACHE DB
    REDIS_URL = str(os.environ.get("REDIS_URL", "redis://localhost:6379/0"))
    REDIS_POOL_SIZE = int(os.environ.get("REDIS_POOL_SIZE", 10))
    REDIS_POOL_TIMEOUT = int(os.environ.get("REDIS_POOL_TIMEOUT", 60))


config = Config()
