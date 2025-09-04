from _typeshed import Incomplete
from camel.messages import BaseMessage as BaseMessage
from camel.types import ChatCompletion as ChatCompletion
from openai import AsyncStream as AsyncStream, Stream as Stream
from pydantic import BaseModel
from typing import Any

class ToolCallRequest(BaseModel):
    tool_name: str
    args: dict[str, Any]
    tool_call_id: str

class ModelResponse(BaseModel):
    model_config: Incomplete
    response: ChatCompletion | Stream | AsyncStream
    tool_call_requests: list[ToolCallRequest] | None
    output_messages: list[BaseMessage]
    finish_reasons: list[str]
    usage_dict: dict[str, Any]
    response_id: str
