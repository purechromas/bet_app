from sqlalchemy import select
from sqlalchemy.dialects.postgresql import insert

from bet_library.infrastructure.pg_helper import PGHelper
from bet_maker.src.models import Bet


class BetsRepository:
    def __init__(self, pg_helper: PGHelper):
        self._pg_helper = pg_helper

    async def create_bet(self, bet: Bet) -> Bet:
        async with await self._pg_helper.get_session() as session:
            session.add(bet)
            await session.commit()
            await session.refresh(bet)
            return bet

    async def get_all_bets(self) -> list[Bet]:
        async with await self._pg_helper.get_session() as session:
            result = await session.execute(select(Bet))
            events = result.scalars().all()
            return list(events)
