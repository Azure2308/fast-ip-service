from pydantic import BaseModel

from app.domain.enums import IPProvidersEnum


class IPResponse(BaseModel):
    myIP: str
    type: IPProvidersEnum


class ErrorResponse(BaseModel):
    error: str
    message: str
