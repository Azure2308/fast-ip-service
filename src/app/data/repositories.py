from sqlalchemy.ext.asyncio import AsyncSession

from app.data.models import Request


class RequestRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def add_record(self, type_: str, ip: str) -> None:
        ip_request = Request(type=type_, ip=ip)
        async with self.session.begin():
            self.session.add(ip_request)
