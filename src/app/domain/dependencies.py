from fastapi import Depends

from app.data.dependencies import get_request_repository
from app.domain.interfaces import IPProviderInterface, IRequestRepository
from app.domain.services import IPService
from app.infrastructure.dependencies import get_ip_provider


async def get_ip_service(
    provider: IPProviderInterface = Depends(get_ip_provider),
    repository: IRequestRepository = Depends(get_request_repository),
) -> IPService:
    return IPService(provider, repository)
