import asyncio

import grpc

from bet_library.infrastructure.pg_helper import PGHelper

from line_provider.config import CONFIG
from line_provider.src.models.base import BaseModel
from line_provider.src.grpc.grpc_api_pb2_grpc import add_LineProviderServiceServicer_to_server
from line_provider.src.grpc.grpc_line_provider_service import EventService
from line_provider.src.repository.events import EventRepository


async def async_main():
    server = grpc.aio.server()

    pg_helper = PGHelper(CONFIG.PG_URL, CONFIG.SQLALCHEMY_ECHO, CONFIG.PG_POOL_SIZE, CONFIG.PG_POOL_TIMEOUT)

    base_model = BaseModel()
    await pg_helper.create_tables(base_model)

    event_repository = EventRepository(pg_helper)

    # Add your service to the server
    add_LineProviderServiceServicer_to_server(EventService(event_repository), server)

    server.add_insecure_port('[::]:50051')  # Bind the server to a specific address and port

    await server.start()  # Start the server
    print("Server started on port 50051")

    await server.wait_for_termination()  # Keep the server running


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()
