from pydantic import BaseModel
from typing import Any

class ToolCallingRecord(BaseModel):
    tool_name: str
    args: dict[str, Any]
    result: Any
    tool_call_id: str
    def as_dict(self) -> dict[str, Any]: ...
