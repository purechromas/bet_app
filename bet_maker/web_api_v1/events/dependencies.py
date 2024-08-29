from fastapi import Request

from bet_maker.web_api_v1.events.schemas import EventsListOut, Event
from bet_library.line_provider_client_grpc import LineProviderClientGRPC

from line_provider.src.grpc import grpc_api_pb2 as pb2


async def get_unfinished_events_handler(request: Request) -> EventsListOut:
    line_provider_client_grpc: LineProviderClientGRPC = request.app.state.line_provider_client_grpc
    grpc_response: pb2.GetListEventsResponse = await line_provider_client_grpc.get_list_events()

    events = [
        Event(
            id=event.id,
            event_name=event.event_name,
            odds=event.odds,
            status=event.status,
            finish_at=event.finish_at,
            created_at=event.created_at,
            updated_at=event.updated_at,
        )
        for event in grpc_response.events
    ]

    return EventsListOut(events=events)
