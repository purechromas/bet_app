import asyncio
from datetime import datetime

import grpc
from line_provider.src.grpc import grpc_api_pb2 as pb2
from line_provider.src.grpc import grpc_api_pb2_grpc as pb2_grpc

async def run():
    async with grpc.aio.insecure_channel('localhost:50051') as channel:
        stub = pb2_grpc.LineProviderServiceStub(channel)

        # Example: GetEvent by ID
        request = pb2.GetEventRequest(id="1")
        response = await stub.GetEvent(request)
        print("GetEvent response:", response)

        # Example: GetEvent by Name
        request = pb2.GetEventRequest(event_name="test")
        response = await stub.GetEvent(request)
        print("GetEvent response:", response)

        # Example: CreateEvent
        create_request = pb2.CreateEventRequest(
            event_name="New Eventa",
            odds=1.55,
            finish_at=datetime.now().isoformat()# Example timestamp
        )
        create_response = await stub.CreateEvent(create_request)
        print("CreateEvent response:", create_response)

        # Example: GetListEvents
        list_request = pb2.GetListEventsRequest()
        list_response = await stub.GetListEvents(list_request)
        print("ListEvents response:", list_response)

        # Example: UpdateEventStatus
        update_request = pb2.UpdateEventStatusRequest(
            id="1",
            status="test"
        )

        update_response = await stub.UpdateEventStatus(update_request)
        print("UpdateEventStatus response:", update_response)

if __name__ == "__main__":
    asyncio.run(run())
