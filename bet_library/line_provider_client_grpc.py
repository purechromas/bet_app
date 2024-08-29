from enum import Enum
from datetime import datetime

import grpc

from line_provider.src.grpc import grpc_api_pb2 as pb2
from line_provider.src.grpc import grpc_api_pb2_grpc as pb2_grpc


class EventStatus(Enum):
    UNFINISHED = "unfinished"
    TEAM_1_WINNER = "team_1_winner"
    TEAM_2_WINNER = "team_2_winner"


class LineProviderClientGRPC:
    def __init__(self, channel: grpc.aio.Channel, stub: pb2_grpc.LineProviderServiceStub):
        self._channel = channel
        self._stub = stub

    async def get_event_by_id(self, event_id: str) -> pb2.GetEventResponse:
        request = pb2.GetEventRequest(id=event_id)
        return await self._stub.GetEvent(request)

    async def get_event_by_name(self, event_name: str) -> pb2.GetEventResponse:
        request = pb2.GetEventRequest(event_name=event_name)
        return await self._stub.GetEvent(request)

    async def create_event(self, event_name: str, odds: float, finish_at: str) -> pb2.CreateEventResponse:
        request = pb2.CreateEventRequest(event_name=event_name, odds=odds, finish_at=finish_at)
        return await self._stub.CreateEvent(request)

    async def get_list_events(self) -> pb2.GetListEventsResponse:
        request = pb2.GetListEventsRequest()
        return await self._stub.GetListEvents(request)

    async def update_event_status(self, event_id: str, status: EventStatus) -> pb2.UpdateEventStatusResponse:
        request = pb2.UpdateEventStatusRequest(id=event_id, status=status.value)
        return await self._stub.UpdateEventStatus(request)
