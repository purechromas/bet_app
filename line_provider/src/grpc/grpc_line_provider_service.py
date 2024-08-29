from datetime import datetime

import grpc

from bet_library.common_errors import NotFoundError

from line_provider.src.models.events import Event
from line_provider.src.grpc import grpc_api_pb2 as pb2
from line_provider.src.grpc import grpc_api_pb2_grpc as pb2_grpc
from line_provider.src.repository.events import EventRepository


class EventService(pb2_grpc.LineProviderServiceServicer):
    def __init__(self, event_repository: EventRepository):
        self._event_repository = event_repository

    async def GetEvent(self, request: pb2.GetEventRequest, context: grpc.ServicerContext) -> pb2.GetEventResponse:
        event_id: str = request.id
        event_name: str = request.event_name

        if event_id:
            try:
                event: Event | None = await self._event_repository.get_event_by_id(event_id)
            except NotFoundError as e:
                context.set_code(grpc.StatusCode.NOT_FOUND)
                context.set_details(str(e))
                return pb2.GetEventResponse()
        elif event_name:
            try:
                event: Event | None = await self._event_repository.get_event_by_name(event_name)
            except NotFoundError as e:
                context.set_code(grpc.StatusCode.NOT_FOUND)
                context.set_details(str(e))
                return pb2.GetEventResponse()
        else:
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details("Either event_id or event_name must be provided")
            return pb2.GetEventResponse()

        if not event:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details(f"Event with that kind of field '{event_id if event_id else event_name}' not found")
            return pb2.GetEventResponse()

        context.set_code(grpc.StatusCode.OK)
        event_response = pb2.Event(
            id=event.id,
            event_name=event.event_name,
            odds=event.odds,
            status=event.status,
            finish_at=event.finish_at.isoformat(),
            created_at=event.created_at.isoformat(),
            updated_at=event.updated_at.isoformat(),
        )
        return pb2.GetEventResponse(event=event_response)

    async def CreateEvent(
        self, request: pb2.CreateEventRequest, context: grpc.ServicerContext
    ) -> pb2.CreateEventResponse:
        event = Event(
            event_name=request.event_name,
            odds=request.odds,
            finish_at=datetime.fromisoformat(request.finish_at),
        )

        event = await self._event_repository.create_event(event)

        response_event = pb2.Event(
            id=event.id,
            event_name=event.event_name,
            odds=event.odds,
            status=event.status,
            finish_at=event.finish_at.isoformat(),
            created_at=event.created_at.isoformat(),
            updated_at=event.updated_at.isoformat(),
        )
        return pb2.CreateEventResponse(event=response_event)

    async def GetListEvents(
        self, request: pb2.GetListEventsRequest, context: grpc.ServicerContext
    ) -> pb2.GetListEventsResponse:
        events: list[Event] = await self._event_repository.get_unfinished_events()

        response_events = [
            pb2.Event(
                id=event.id,
                event_name=event.event_name,
                odds=event.odds,
                status=event.status,
                finish_at=event.finish_at.isoformat(),
                created_at=event.created_at.isoformat(),
                updated_at=event.updated_at.isoformat(),
            )
            for event in events
        ]

        context.set_code(grpc.StatusCode.OK)
        return pb2.GetListEventsResponse(events=response_events)

    async def UpdateEventStatus(
        self, request: pb2.UpdateEventStatusRequest, context: grpc.ServicerContext
    ) -> pb2.UpdateEventStatusResponse:
        event_id: str = request.id
        status: str = request.status

        try:
            event: Event = await self._event_repository.update_event_status(event_id, status)
        except NotFoundError as e:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details(str(e))
            return pb2.google_dot_protobuf_dot_empty__pb2()

        context.set_code(grpc.StatusCode.OK)
        response_event = pb2.Event(
            id=event.id,
            event_name=event.event_name,
            odds=event.odds,
            status=event.status,
            finish_at=event.finish_at.isoformat(),
            created_at=event.created_at.isoformat(),
            updated_at=event.updated_at.isoformat(),
        )
        return pb2.UpdateEventStatusResponse(event=response_event)
