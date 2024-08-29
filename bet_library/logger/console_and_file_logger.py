import os
import logging

from logging import handlers


def configure_console_and_file_logger(
    console_log_level: str,
    file_log_level: str,
    path_name: str,
    file_name: str,
    max_file_size: int = 1024 * 50,  # 50 МБ
):
    # Создаем логгер и добавляем левел отладки
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    # Создаем обработчик для консоли
    console_handler = logging.StreamHandler()
    console_handler.setLevel(console_log_level)  # Устанавливаем уровень для консоли

    # Создаем директорию для логов, если она не существует
    log_dir = os.path.join(path_name, "logs")
    os.makedirs(log_dir, exist_ok=True)

    # Создаем обработчик для файлов
    file_path = os.path.join(log_dir, file_name)
    file_handler = handlers.RotatingFileHandler(filename=file_path, maxBytes=max_file_size)
    file_handler.setLevel(file_log_level)  # Устанавливаем уровень для файлов

    # Создаем форматтер и добавляем его к обработчикам
    formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    # Добавляем обработчики к логгеру
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
