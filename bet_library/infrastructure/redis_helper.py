from redis.asyncio import Redis
from contextlib import asynccontextmanager


class RedisHelper:
    """
    Функционал класса:
    - Открытие соединения с Redis сервером
    - Получение подключения - get_connection()
    """

    def __init__(
        self,
        redis_url: str,  # URL для подключения к Redis серверу
        redis_pool: int = 5,  # Максимальное количество подключений в пуле
        redis_pool_timeout: int | None = None,  # Тайм-аут ожидания подключения из пула в секундах
    ):
        self._redis = Redis.from_url(
            redis_url,
            max_connections=redis_pool,
            pool_timeout=redis_pool_timeout,
        )

    @asynccontextmanager
    async def get_connection(self) -> Redis:
        """
        Асинхронный менеджер контекста для получения подключения из пула Redis.

        Использование:
        async with redis_helper.get_connection() as conn:
            # Используйте `conn` для выполнения операций с Redis
            await conn.set('key', 'value')
        """
        conn = await self._redis.client()
        try:
            yield conn
        finally:
            await conn.close()  # Закрытие подключения и возврат его в пул
