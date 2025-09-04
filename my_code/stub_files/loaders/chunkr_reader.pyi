from _typeshed import Incomplete
from typing import Any

logger: Incomplete

class ChunkrReader:
    timeout: Incomplete
    def __init__(self, api_key: str | None = None, url: str | None = 'https://api.chunkr.ai/api/v1/task', timeout: int = 30, **kwargs: Any) -> None: ...
    def submit_task(self, file_path: str, model: str = 'Fast', ocr_strategy: str = 'Auto', target_chunk_length: str = '512') -> str: ...
    def get_task_output(self, task_id: str, max_retries: int = 5) -> str: ...
