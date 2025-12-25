from fastapi import APIRouter, Depends

from app.domain.dependencies import get_ip_service
from app.domain.services import IPService
from app.presentation.handlers import IPHandlers
from app.presentation.schemas import IPResponse, ErrorResponse

ip_router = APIRouter(prefix='', tags=['IP'])


@ip_router.get(
    '/ip',
    response_model=IPResponse,
    responses={502: {'model': ErrorResponse, 'description': 'Не удалось загрузить IP'}},
)
async def get_ip(service: IPService = Depends(get_ip_service)):
    handler = IPHandlers(service)
    return await handler.get_ip()
