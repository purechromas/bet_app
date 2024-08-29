import asyncio
import logging

import grpc
import uvicorn

from fastapi import FastAPI

from bet_library.common_amqp import publish_message_in_default_exc
from bet_maker.src.settings.config import config
from bet_maker.src.settings.lifespan import lifespan
from bet_maker.web_api_v1.bets.endpoints import bets_router
from bet_maker.web_api_v1.events.endpoints import events_router

log = logging.getLogger(__name__)


def init_api() -> FastAPI:
    fast_api = FastAPI(
        title=config.APP_NAME,
        docs_url="/",
        lifespan=lifespan,
    )

    fast_api.include_router(events_router)
    fast_api.include_router(bets_router)

    return fast_api


def main():
    app: FastAPI = init_api()
    try:
        uvicorn.run(
            app,
            host=config.APP_HOST,
            port=config.APP_PORT,
        )
    except grpc.RpcError as e:
        log.error(str(e))
    # Кроме фатальных ошибок, мы можем ловить и те, которые ожидаем (например, от RabbitMQ, Redis, Postgres, gRPC).
    except Exception as e:
        # Фатальные ошибки логируем в консоль и файл, а также отправляем в RabbitMQ
        log.exception(f"Fatal error {e}")
        event_loop = asyncio.get_event_loop()
        amqp_channel = app.state.amqp_channel
        event_loop.create_task(publish_message_in_default_exc(amqp_channel, str(e), config.AMQP_ROUTING_KEY_LOGGER))


if __name__ == "__main__":
    main()
