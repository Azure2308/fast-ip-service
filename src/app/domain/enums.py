from enum import Enum


class IPProvidersEnum(str, Enum):
    IPAPI = 'IPAPI'
    JSONIP = 'JSONIP'

    @property
    def url(self) -> str:
        return {
            'IPAPI': 'http://ip-api.com/json/',
            'JSONIP': 'https://jsonip.com/',
        }[self.value]
