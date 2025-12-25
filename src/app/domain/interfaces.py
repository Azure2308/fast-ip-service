from typing import Protocol

from app.domain.entities import IPAddress


class IPProviderInterface(Protocol):
    async def fetch_ip(self) -> IPAddress: ...


class IRequestRepository(Protocol):
    async def add_record(self, type_: str, ip: str) -> None: ...
