from abc import ABC, abstractmethod
from pydantic import BaseModel
from typing import Any

class VectorRecord(BaseModel):
    vector: list[float]
    id: str
    payload: dict[str, Any] | None

class VectorDBQuery(BaseModel):
    query_vector: list[float]
    top_k: int
    def __init__(self, query_vector: list[float], top_k: int, **kwargs: Any) -> None: ...

class VectorDBQueryResult(BaseModel):
    record: VectorRecord
    similarity: float
    @classmethod
    def create(cls, similarity: float, vector: list[float], id: str, payload: dict[str, Any] | None = None) -> VectorDBQueryResult: ...

class VectorDBStatus(BaseModel):
    vector_dim: int
    vector_count: int

class BaseVectorStorage(ABC):
    @abstractmethod
    def add(self, records: list[VectorRecord], **kwargs: Any) -> None: ...
    @abstractmethod
    def delete(self, ids: list[str], **kwargs: Any) -> None: ...
    @abstractmethod
    def status(self) -> VectorDBStatus: ...
    @abstractmethod
    def query(self, query: VectorDBQuery, **kwargs: Any) -> list[VectorDBQueryResult]: ...
    @abstractmethod
    def clear(self) -> None: ...
    @abstractmethod
    def load(self) -> None: ...
    @property
    @abstractmethod
    def client(self) -> Any: ...
    def get_payloads_by_vector(self, vector: list[float], top_k: int) -> list[dict[str, Any]]: ...
