from abc import ABC, abstractmethod
from typing import Any

class BaseAgent(ABC):
    @abstractmethod
    def reset(self, *args: Any, **kwargs: Any) -> Any: ...
    @abstractmethod
    def step(self, *args: Any, **kwargs: Any) -> Any: ...
