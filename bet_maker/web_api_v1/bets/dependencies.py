import json
import logging

import grpc

from fastapi import Request, HTTPException
from grpc.aio import AioRpcError

from bet_maker.src.models import Bet
from bet_maker.src.repositories.bets import BetsRepository
from bet_maker.web_api_v1.bets.schemas import CreateBetOut, CreateBetIn, BetOut

from bet_library.infrastructure.pg_helper import PGHelper
from bet_library.line_provider_client_grpc import LineProviderClientGRPC

from line_provider.src.grpc import grpc_api_pb2 as pb2

log = logging.getLogger(__name__)


async def create_bet_handler(request: Request, bet_data: CreateBetIn) -> CreateBetOut:
    line_provider_client_grpc: LineProviderClientGRPC = request.app.state.line_provider_client_grpc
    try:
        await line_provider_client_grpc.get_event_by_id(event_id=bet_data.event_id)
    except AioRpcError as e:
        error_info = {
            "status": e.code().name,
            "info": e.details(),
        }
        log.exception("Error in update_event_status: %s", json.dumps(error_info))
        if e.code() == grpc.StatusCode.NOT_FOUND:
            raise HTTPException(status_code=404, detail="Doesn't exist that kind of event")
        else:
            raise HTTPException(status_code=500, detail="Something get wrong")

    pg_helper: PGHelper = request.app.state.pg_helper
    bet_repository = BetsRepository(pg_helper)

    bet = Bet(
        event_id=bet_data.event_id,
        amount=bet_data.amount,
    )
    created_bet = await bet_repository.create_bet(bet)
    return CreateBetOut(bet_id=created_bet.id)


async def get_all_bets_handler(request: Request) -> list[BetOut]:
    pg_helper: PGHelper = request.app.state.pg_helper
    bet_repository = BetsRepository(pg_helper)
    all_bets: list[Bet] = await bet_repository.get_all_bets()
    bets = [
        BetOut(
            bet_id=bet.id,
            event_id=bet.event_id,
            amount=bet.amount,
            status=bet.status,
            created_at=bet.created_at.isoformat(),
        )
        for bet in all_bets
    ]
    return bets
