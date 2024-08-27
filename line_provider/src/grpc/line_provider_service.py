import grpc

from line_provider.src.models.events import Event
import grpc_api_pb2 as pb2
import grpc_api_pb2_grpc as pb2_grpc
from line_provider.src.repository.events import EventRepository


class EventService(pb2_grpc.LineProviderServiceServicer):
    def __init__(self, event_repository: EventRepository):
        self._event_repository = event_repository

    async def GetEvent(self, request, context):
        event: Event | None = None

        event_id: str = request.id
        event_name: str = request.event_name

        if event_id:
            event: Event | None = await self._event_repository.get_event_by_id(event_id)
        elif event_name:
            event: Event | None = await self._event_repository.get_event_by_name(event_name)
        else:
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details("Either event_id or event_name must be provided")
            return pb2.GetEventResponse()

        if not event:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details(f"Event with that kind of field '{event_id if event_id else event_name}' not found")
            return pb2.GetEventResponse()

        context.set_code(grpc.StatusCode.OK)
        return pb2.GetEventResponse(
            pb2.Event(
                id=event.id,
                event_name=event.event_name,
                odds=event.odds,
                status=event.status,
                finish_at=event.finish_at,
                created_at=event.created_at,
                updated_at=event.updated_at
            )
        )
