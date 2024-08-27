from sqlalchemy import select

from bet_library.common_exceptions import NotFoundError
from bet_library.infrastructure.pg_helper import PGHelper

from line_provider.src.models.events import Event


class EventRepository:
    def __init__(
            self,
            pg_helper: PGHelper
    ):
        self._pg_helper = pg_helper

    async def get_event_by_id(self, event_id: str) -> Event | None:
        async with await self._pg_helper.get_session() as session:
            query = select(Event).where(Event.id == event_id)
            result = await session.execute(query)
            event = result.scalars().first()

            if not event:
                raise NotFoundError(f"Event with id {event_id} was not found.")

            return event

    async def get_event_by_name(self, event_name: str) -> Event | None:
        async with await self._pg_helper.get_session() as session:
            query = select(Event).where(Event.event_name == event_name)
            result = await session.execute(query)
            event = result.scalars().first()

            if not event:
                raise NotFoundError(f"Event with name {event_name} was not found.")

            return event
