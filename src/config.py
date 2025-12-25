from dotenv import load_dotenv
from pydantic_settings import BaseSettings

from app.domain.enums import IPProvidersEnum

load_dotenv()


class Settings(BaseSettings):
    type: IPProvidersEnum
    port: int
    postgres_user: str
    postgres_password: str
    postgres_db: str
    postgres_host: str
    postgres_port: int

    class Config:
        env_file = '.env'


settings = Settings()
