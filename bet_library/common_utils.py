import re
import uuid

from datetime import datetime


def camel_case_2_snake_case(camel_case: str) -> str:
    """Преобразуем SomeWord(CamelCase) в some_word(snake_case)"""
    return re.sub(r"(?<!^)(?=[A-Z])", "_", camel_case).lower()


def generate_uuid() -> str:
    """Генерация нового уникального идентификатора UUID."""
    return str(uuid.uuid4())


def get_utc_time_now_isodate() -> datetime:
    """Возвращает текущее время в формате ISO 8601."""
    return datetime.utcnow()
