import logging

from contextlib import asynccontextmanager

import aio_pika
import grpc

from fastapi import FastAPI

from bet_library.common_amqp import create_amqp_queue
from bet_maker.src.settings.config import config
from bet_maker.src.models.base import BaseModel

from bet_library.infrastructure.pg_helper import PGHelper
from bet_library.line_provider_client_grpc import LineProviderClientGRPC
from bet_library.logger.console_and_file_logger import configure_console_and_file_logger

from line_provider.src.grpc import grpc_api_pb2_grpc as pb2_grpc

log = logging.getLogger(config.APP_NAME)


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Init postgres
    pg_helper = PGHelper(config.PG_URL)
    base = BaseModel()
    await pg_helper.create_tables(base)

    # Init connection with line provider service by GRPC
    channel_grpc = grpc.aio.insecure_channel(config.LINE_PROVIDER_GRPC_SERVER_URL)
    stub = pb2_grpc.LineProviderServiceStub(channel_grpc)
    line_provider_client_grpc = LineProviderClientGRPC(channel_grpc, stub)

    # Init connection with RabbitMQ
    amqp_connection = await aio_pika.connect(config.AMQP_URL)
    amqp_channel = await amqp_connection.channel()
    await create_amqp_queue(amqp_channel, config.AMQP_ROUTING_KEY_LOGGER)

    # Init logging settings
    configure_console_and_file_logger(
        console_log_level=config.CONSOLE_LOG_LEVEL,
        file_log_level=config.FILE_LOG_LEVEL,
        path_name=config.BASE_DIR,
        file_name=config.APP_NAME,
    )

    # Add all singleton instances in app, so we can use them in all the app.
    app.state.pg_helper = pg_helper
    app.state.line_provider_client_grpc = line_provider_client_grpc
    app.state.amqp_channel = amqp_channel

    log.info("Application started and it was properly configuration")
    yield
    log.info("Application was turned off, closing all connections")
    await pg_helper.dispose_engine()
    await channel_grpc.close()
