from _typeshed import Incomplete
from camel.utils.chunker import BaseChunker
from unstructured.documents.elements import Element as Element

class UnstructuredIOChunker(BaseChunker):
    uio: Incomplete
    chunk_type: Incomplete
    max_characters: Incomplete
    metadata_filename: Incomplete
    def __init__(self, chunk_type: str = 'chunk_by_title', max_characters: int = 500, metadata_filename: str | None = None) -> None: ...
    def chunk(self, content: list['Element']) -> list['Element']: ...
