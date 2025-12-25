from fastapi import Depends, Request

from app.infrastructure.client import HttpClient
from app.infrastructure.provider import IPProvider


async def get_http_client(request: Request) -> HttpClient:
    return request.app.state.http_client


async def get_ip_provider(client: HttpClient = Depends(get_http_client)) -> IPProvider:
    return IPProvider(client)
