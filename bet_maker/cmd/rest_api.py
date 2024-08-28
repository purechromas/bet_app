import uvicorn
from fastapi import FastAPI
from app.web.api_v1.auth.endpoints import auth_routers
from app.web.api_v1.project.endpoints import project_routers
from app.settings.config_app import settings
from app.settings.config_lifespan import lifespan


def init_api() -> FastAPI:
    fast_api = FastAPI(
        title="Bet Maker Rest API",
        docs_url="/",
        lifespan=lifespan,
    )
    fast_api.include_router(auth_routers)
    fast_api.include_router(project_routers)
    return fast_api


def main():
    uvicorn.run(
        "app.cmd.restapi:init_api",
        host=settings.APP_HOST,
        port=settings.APP_PORT,
        reload=settings.DEBUG
    )


if __name__ == "__main__":
    main()