from camel.embeddings.base import BaseEmbedding as BaseEmbedding
from pydantic import BaseModel
from typing import Literal

class DeduplicationResult(BaseModel):
    original_texts: list[str]
    unique_ids: list[int]
    unique_embeddings_dict: dict[int, list[float]]
    duplicate_to_target_map: dict[int, int]

def deduplicate_internally(texts: list[str], threshold: float = 0.65, embedding_instance: BaseEmbedding[str] | None = None, embeddings: list[list[float]] | None = None, strategy: Literal['top1', 'llm-supervise'] = 'top1', batch_size: int = 1000) -> DeduplicationResult: ...
