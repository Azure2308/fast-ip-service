from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.infrastructure.client import HttpClient
from app.presentation.routers import ip_router
from config import settings


def get_api() -> FastAPI:
    @asynccontextmanager
    async def lifespan(app: FastAPI):
        http_client = HttpClient(url=settings.type.url, name=settings.type.name)
        await http_client.init_session()
        app.state.http_client = http_client
        yield
        await http_client.close_session()

    app = FastAPI(lifespan=lifespan)
    app.include_router(ip_router)
    return app


app = get_api()
