import asyncio
import logging

import aio_pika
import grpc

from bet_library.infrastructure.pg_helper import PGHelper
from bet_library.common_amqp import publish_message_in_default_exc, create_amqp_queue
from bet_library.logger.console_and_file_logger import configure_console_and_file_logger

from line_provider.src.config import config
from line_provider.src.models.base import BaseModel
from line_provider.src.grpc.grpc_api_pb2_grpc import (
    add_LineProviderServiceServicer_to_server,
)
from line_provider.src.grpc.grpc_line_provider_service import EventService
from line_provider.src.repository.events import EventRepository

log = logging.getLogger(__name__)


async def async_main():
    pg_helper = PGHelper(
        config.PG_URL,
        config.SQLALCHEMY_ECHO,
        config.PG_POOL_SIZE,
        config.PG_POOL_TIMEOUT,
    )
    base_model = BaseModel()
    await pg_helper.create_tables(base_model)

    event_repository = EventRepository(pg_helper)

    configure_console_and_file_logger(
        console_log_level=config.CONSOLE_LOG_LEVEL,
        file_log_level=config.FILE_LOG_LEVEL,
        path_name=config.BASE_DIR,
        file_name=config.APP_NAME,
    )

    amqp_connection = await aio_pika.connect(config.AMQP_URL)
    amqp_channel = await amqp_connection.channel()
    await create_amqp_queue(amqp_channel, config.AMQP_ROUTING_KEY_LOGGER)

    server = grpc.aio.server()

    add_LineProviderServiceServicer_to_server(EventService(event_repository), server)

    server.add_insecure_port(f"{config.APP_GRPC_HOST}:{config.APP_GRPC_PORT}")

    try:
        log.info(f"Server started on port {config.APP_GRPC_PORT}")
        await server.start()
        await server.wait_for_termination()
    except grpc.RpcError as e:
        log.error(str(e))
    # Кроме фатальных ошибок, мы можем ловить и те, которые ожидаем (например, от RabbitMQ, Redis, Postgres, gRPC).
    except Exception as e:
        # Фатальные ошибки логируем в консоль и файл, а также отправляем в RabbitMQ
        log.exception(f"Fatal error {e}")
        await publish_message_in_default_exc(amqp_channel, str(e), routing_key=config.AMQP_ROUTING_KEY_LOGGER)


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()
