from abc import ABC, abstractmethod
from typing import Any

class BaseKeyValueStorage(ABC):
    @abstractmethod
    def save(self, records: list[dict[str, Any]]) -> None: ...
    @abstractmethod
    def load(self) -> list[dict[str, Any]]: ...
    @abstractmethod
    def clear(self) -> None: ...
