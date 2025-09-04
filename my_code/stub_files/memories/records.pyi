from _typeshed import Incomplete
from camel.messages import BaseMessage, OpenAIMessage
from camel.types import OpenAIBackendRole
from pydantic import BaseModel
from typing import Any
from uuid import UUID

class MemoryRecord(BaseModel):
    model_config: Incomplete
    message: BaseMessage
    role_at_backend: OpenAIBackendRole
    uuid: UUID
    extra_info: dict[str, str]
    timestamp: float
    agent_id: str
    @classmethod
    def from_dict(cls, record_dict: dict[str, Any]) -> MemoryRecord: ...
    def to_dict(self) -> dict[str, Any]: ...
    def to_openai_message(self) -> OpenAIMessage: ...

class ContextRecord(BaseModel):
    memory_record: MemoryRecord
    score: float
    timestamp: float
