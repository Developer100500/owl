from camel.types.enums import JinaReturnFormat
from typing import Any

JINA_ENDPOINT: str

class JinaURLReader:
    def __init__(self, api_key: str | None = None, return_format: JinaReturnFormat = ..., json_response: bool = False, timeout: int = 30, **kwargs: Any) -> None: ...
    def read_content(self, url: str) -> str: ...
