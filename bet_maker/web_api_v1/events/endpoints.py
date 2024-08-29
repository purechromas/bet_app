from datetime import datetime
from typing import Annotated

from fastapi import APIRouter, Depends, Request, Body, status
from pydantic import BaseModel, Field

from bet_library.line_provider_client_grpc import LineProviderClientGRPC
from bet_maker.web_api_v1.events.dependencies import get_unfinished_events_handler
from bet_maker.web_api_v1.events.schemas import EventsListOut, Event

events_router = APIRouter(prefix="/events", tags=["events"])


@events_router.get("/", status_code=status.HTTP_200_OK)
async def get_unfinished_events(
        events_list: EventsListOut = Depends(get_unfinished_events_handler),
) -> EventsListOut:
    return events_list


class CreateEventIn(BaseModel):
    event_name: str
    odds: float = Field(gt=0, description="Amount must be a positive number with two decimal places")
    finish_at: datetime


async def create_event_handler(request: Request, event_data: CreateEventIn) -> Event:
    line_provider_client_grpc: LineProviderClientGRPC = request.app.state.line_provider_client_grpc

    grpc_response = await line_provider_client_grpc.create_event(event_data.event_name, event_data.odds, event_data.finish_at.isoformat())
    return Event(
        id=grpc_response.event.id,
        event_name=grpc_response.event.event_name,
        odds=grpc_response.event.odds,
        status=grpc_response.event.status,
        finish_at=grpc_response.event.finish_at,
        created_at=grpc_response.event.created_at,
        updated_at=grpc_response.event.updated_at,
    )

@events_router.post("/", status_code=status.HTTP_201_CREATED)
async def create_event(request: Request, event_data: Annotated[CreateEventIn, Body()]) -> Event:
    return await create_event_handler(request, event_data)
