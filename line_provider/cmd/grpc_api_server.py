import asyncio
from concurrent import futures

import grpc

from bet_library.infrastructure.pg_helper import PGHelper


from line_provider.config import CONFIG
from line_provider.src.models.base import BaseModel
from grpc_api_pb2_grpc import add_LineProviderServiceServicer_to_server

from line_provider.src.grpc.line_provider_service import EventService
from line_provider.src.repository.events import EventRepository

async def init_pg_db():
    pg_helper = PGHelper(CONFIG.PG_URL, CONFIG.SQLALCHEMY_ECHO, CONFIG.PG_POOL_SIZE, CONFIG.PG_POOL_TIMEOUT)
    await pg_helper.init_db(BaseModel())

async def async_main():
    server = grpc.aio.server(futures.ThreadPoolExecutor(max_workers=10))

    base_model = BaseModel()
    pg_helper = PGHelper(CONFIG.PG_URL, CONFIG.SQLALCHEMY_ECHO, CONFIG.PG_POOL_SIZE, CONFIG.PG_POOL_TIMEOUT)
    await pg_helper.init_db(base_model)

    event_repository = EventRepository(pg_helper)
    # Add your service to the server
    add_LineProviderServiceServicer_to_server(
        EventService(event_repository), server)

    # Bind the server to a specific address and port
    server.add_insecure_port('[::]:50051')

    # Start the server
    await server.start()
    print("Server started on port 50051")

    # Keep the server running
    await server.wait_for_termination()

def main():
    asyncio.run(async_main())

if __name__ == "__main__":
    main()
