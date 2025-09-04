from _typeshed import Incomplete
from abc import ABC, abstractmethod
from io import BytesIO
from typing import Any

def create_file(file: BytesIO, filename: str) -> File: ...
def create_file_from_raw_bytes(raw_bytes: bytes, filename: str) -> File: ...

class File(ABC):
    name: Incomplete
    file_id: Incomplete
    metadata: Incomplete
    docs: Incomplete
    raw_bytes: Incomplete
    def __init__(self, name: str, file_id: str, metadata: dict[str, Any] | None = None, docs: list[dict[str, Any]] | None = None, raw_bytes: bytes = b'') -> None: ...
    @classmethod
    @abstractmethod
    def from_bytes(cls, file: BytesIO, filename: str) -> File: ...
    @classmethod
    def from_raw_bytes(cls, raw_bytes: bytes, filename: str) -> File: ...
    def copy(self) -> File: ...

def strip_consecutive_newlines(text: str) -> str: ...

class DocxFile(File):
    @classmethod
    def from_bytes(cls, file: BytesIO, filename: str) -> DocxFile: ...

class PdfFile(File):
    @classmethod
    def from_bytes(cls, file: BytesIO, filename: str) -> PdfFile: ...

class TxtFile(File):
    @classmethod
    def from_bytes(cls, file: BytesIO, filename: str) -> TxtFile: ...

class JsonFile(File):
    @classmethod
    def from_bytes(cls, file: BytesIO, filename: str) -> JsonFile: ...

class HtmlFile(File):
    @classmethod
    def from_bytes(cls, file: BytesIO, filename: str) -> HtmlFile: ...
