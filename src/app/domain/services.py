from app.domain.entities import IPAddress
from app.domain.interfaces import IPProviderInterface, IRequestRepository


class IPService:
    def __init__(self, provider: IPProviderInterface, repository: IRequestRepository) -> None:
        self.provider = provider
        self.repository = repository

    async def get_ip(self) -> IPAddress:
        ip_data = await self.provider.fetch_ip()
        await self.repository.add_record(type_=ip_data.api_type, ip=ip_data.value)
        return ip_data
