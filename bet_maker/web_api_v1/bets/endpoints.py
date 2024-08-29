from typing import Annotated

from fastapi import APIRouter, Request, Body, status

from bet_maker.web_api_v1.bets.dependencies import (
    create_bet_handler,
    get_all_bets_handler,
)
from bet_maker.web_api_v1.bets.schemas import CreateBetOut, CreateBetIn, BetOut

bets_router = APIRouter(prefix="/bets", tags=["bets"])


@bets_router.post("/", status_code=status.HTTP_201_CREATED)
async def create_bet(request: Request, bet_data: Annotated[CreateBetIn, Body()]) -> CreateBetOut:
    return await create_bet_handler(request, bet_data)


@bets_router.get("/", status_code=status.HTTP_200_OK)
async def get_all_bets(request: Request) -> list[BetOut]:
    return await get_all_bets_handler(request)
