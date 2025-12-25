from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.data.database import get_session
from app.data.repositories import RequestRepository


async def get_request_repository(session: AsyncSession = Depends(get_session)) -> RequestRepository:
    return RequestRepository(session)
