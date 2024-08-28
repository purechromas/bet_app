import os

from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
from dataclasses import dataclass


@dataclass(frozen=True)
class Config:
    # БЕЗ ПЕРЕМЕННЫХ ОКРУЖЕНИЯ 🔴
    APP_NAME = "line_provider"
    APP_VERSION = "0.0.1"
    BASE_DIR = Path(__file__).resolve().parent.parent
    TIME_MOSCOW_NOW = datetime.now(ZoneInfo('Europe/Moscow'))

    # С ПЕРЕМЕННЫМИ ОКРУЖЕНИЯ ✅
    BM_REST_API_PORT = int(os.environ.get("BM_REST_API_PORT", 8000))  # BET MAKER REST API (SERVICE)

    # POSTGRES DB
    PG_URL = str(os.environ.get("POSTGRES_URL", "postgresql+asyncpg://qwe123:qwe123@localhost:5432/line_provider"))
    PG_POOL_SIZE = int(os.environ.get("PG_POOL_SIZE", 10))
    PG_POOL_TIMEOUT = int(os.environ.get("PG_POOL_TIMEOUT", 60))

    # ORM
    SQLALCHEMY_ECHO = bool(os.environ.get("SQLALCHEMY_ECHO", 1))

    # REDIS CACHE DB
    REDIS_URL = str(os.environ.get("REDIS_URL", "redis://localhost:6379/0"))
    REDIS_POOL_SIZE = int(os.environ.get("REDIS_POOL_SIZE", 10))
    REDIS_POOL_TIMEOUT = int(os.environ.get("REDIS_POOL_TIMEOUT", 60))


CONFIG = Config()
