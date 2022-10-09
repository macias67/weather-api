from abc import ABC, abstractmethod
from typing import Any


class ProviderInterface(ABC):

    @abstractmethod
    def fetch_info(self, city_name: str) -> Any:
        pass
