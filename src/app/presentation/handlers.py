from fastapi import HTTPException, status

from app.domain.services import IPService
from app.presentation.schemas import IPResponse


class IPHandlers:
    def __init__(self, service: IPService) -> None:
        self.service = service

    async def get_ip(self) -> IPResponse:
        try:
            ip_entity = await self.service.get_ip()
            if not ip_entity.value:
                raise HTTPException(status_code=status.HTTP_502_BAD_GATEWAY, detail='Получен пустой IP')
            return IPResponse(myIP=ip_entity.value, type=ip_entity.api_type)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_502_BAD_GATEWAY, detail=f'Не удалось получить IP: {e}')
