from sqlalchemy import Column, DateTime, Enum, Integer
from sqlalchemy.dialects.postgresql import INET
from sqlalchemy.sql import func

from app.data.database import Base
from app.domain.enums import IPProvidersEnum


class Request(Base):
    __tablename__ = 'requests'

    id = Column(Integer, primary_key=True)
    type = Column(Enum(IPProvidersEnum), nullable=False)
    ip = Column(INET, nullable=False)
    date = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
