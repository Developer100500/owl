from _typeshed import Incomplete
from camel.embeddings import BaseEmbedding as BaseEmbedding
from camel.memories.base import MemoryBlock
from camel.memories.records import ContextRecord, MemoryRecord
from camel.storages.vectordb_storages import BaseVectorStorage as BaseVectorStorage

class VectorDBBlock(MemoryBlock):
    embedding: Incomplete
    vector_dim: Incomplete
    storage: Incomplete
    def __init__(self, storage: BaseVectorStorage | None = None, embedding: BaseEmbedding | None = None) -> None: ...
    def retrieve(self, keyword: str, limit: int = 3) -> list[ContextRecord]: ...
    def write_records(self, records: list[MemoryRecord]) -> None: ...
    def clear(self) -> None: ...
