from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker, AsyncEngine
from sqlalchemy.orm import DeclarativeBase


class PGHelper:
    """
    Функционал класса:
    - Открытие соединения с базой данных
    - Создает и возвращает асинхронную сессию - get_session()
    - Создание таблиц в базе данных - init_db()
    - Закрытие соединения с базой данных - dispose_engine()
    """

    def __init__(
            self,
            url: str,  # URL для подключения к базе данных Postgres.
            echo: bool = False,  # Включение вывода SQL-запросов в лог.
            pool_size: int = 10,  # Максимальное количество подключений в пуле.
            pool_timeout: int = 60,  # Тайм-аут ожидания подключения из пула в секундах.
    ):
        self._engine = create_async_engine(
            url=url,
            echo=echo,
            pool_size=pool_size,
            pool_timeout=pool_timeout,
        )

    async def get_session(
            self,
            auto_flush: bool = False,  # Автоматически сбрасывать изменения перед выполнением запросов.
            auto_commit: bool = False,  # Автоматически фиксировать изменения в базе данных.
            expire_on_commit: bool = False  # Истекать объекты после коммита.
    ) -> AsyncSession:
        session_factory = async_sessionmaker(
            bind=self._engine,
            autoflush=auto_flush,
            autocommit=auto_commit,
            expire_on_commit=expire_on_commit,
        )
        return session_factory()

    async def create_tables(self, declarative_base: DeclarativeBase):
        async with self._engine.begin() as conn:
            await conn.run_sync(declarative_base.metadata.create_all)

    async def dispose_engine(self):
        await self._engine.dispose()
