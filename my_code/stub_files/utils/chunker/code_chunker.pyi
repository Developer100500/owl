from .base import BaseChunker
from _typeshed import Incomplete
from unstructured.documents.elements import Element

class CodeChunker(BaseChunker):
    chunk_size: Incomplete
    tokenizer: Incomplete
    remove_image: Incomplete
    struct_pattern: Incomplete
    image_pattern: Incomplete
    def __init__(self, chunk_size: int = 8192, model_name: str = 'cl100k_base', remove_image: bool | None = True) -> None: ...
    def count_tokens(self, text: str): ...
    def chunk(self, content: list[str]) -> list['Element']: ...
