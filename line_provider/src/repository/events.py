from datetime import timedelta

from sqlalchemy import select, update

from bet_library.common_errors import NotFoundError
from bet_library.common_utils import get_moscow_time_now_isodate
from bet_library.infrastructure.pg_helper import PGHelper

from line_provider.src.models.events import Event


class EventRepository:
    def __init__(self, pg_helper: PGHelper):
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

    async def create_event(self, event: Event) -> Event:
        async with await self._pg_helper.get_session() as session:
            session.add(event)
            await session.commit()
            await session.refresh(event)
            return event

    async def get_unfinished_events(self) -> list[Event]:
        """
        Получить события, у которых осталось больше 1 минуты до финала.

        Понятно, что для этого нужно разработать определенное решение и обратиться к
        продукт-менеджеру для уточнения требований.
        """
        async with await self._pg_helper.get_session() as session:
            result = await session.execute(select(Event).where(
                Event.finish_at > get_moscow_time_now_isodate() - timedelta(minutes=1))
            )
            events = result.scalars().all()
            return events

    async def update_event_status(self, event_id: str, status: str) -> Event:
        async with await self._pg_helper.get_session() as session:
            update_query = (
                update(Event)
                .where(Event.id == event_id)
                .values(status=status)
                .returning(Event)
            )
            result = await session.execute(update_query)
            event = result.scalars().one_or_none()

            if event is None:
                raise NotFoundError(f"Event with ID {event_id} not found, cant update")

            return event
