from curl_cffi import AsyncSession
from curl_cffi.requests.exceptions import HTTPError, RequestException

from app.domain.exceptions import InvalidServiceResponseError, UnavailableServiceError, ExternalServiceError


class HttpClient:
    def __init__(self, url: str, name: str):
        self.session: AsyncSession | None = None
        self.url = url
        self.name = name

    async def init_session(self) -> None:
        self.session = AsyncSession(base_url=self.url)
        self.session.impersonate = 'chrome123'

    async def close_session(self):
        if self.session:
            await self.session.close()

    async def get_ip(self) -> dict[str, str]:
        try:
            response = await self.session.get('')
            response.raise_for_status()
            return response.json()
        except HTTPError as e:
            raise InvalidServiceResponseError(f'Ошибка при отправке запроса: {e.response.status_code}') from e
        except RequestException as e:
            raise UnavailableServiceError(f'Таймаут подключения или сервис недоступен: {e.__class__.__name__}') from e
        except Exception as e:
            raise ExternalServiceError(f'Неожиданная ошибка при отправке запроса: {e.__class__.__name__}') from e
