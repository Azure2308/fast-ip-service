from app.domain.entities import IPAddress
from app.domain.interfaces import IPProviderInterface
from app.infrastructure.client import HttpClient


class IPProvider(IPProviderInterface):
    def __init__(self, http_client: HttpClient) -> None:
        self.http_client = http_client

    async def fetch_ip(self) -> IPAddress:
        data = await self.http_client.get_ip()
        api_type = self.http_client.name
        if api_type == 'IPAPI':
            ip = data.get('query')
        elif api_type == 'JSONIP':
            ip = data.get('ip')
        else:
            raise ValueError('Некорректный тип источника данных')
        return IPAddress(value=ip, api_type=api_type)
