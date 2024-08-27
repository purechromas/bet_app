import re
import uuid


def camel_case_2_snake_case(camel_case: str) -> str:
    """Преобразуем SomeWord(CamelCase) в some_word(snake_case)"""
    return re.sub(r'(?<!^)(?=[A-Z])', '_', camel_case).lower()


def generate_uuid() -> str:
    """Генерация нового уникального идентификатора UUID."""
    return str(uuid.uuid4())
