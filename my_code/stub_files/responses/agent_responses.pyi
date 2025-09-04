from _typeshed import Incomplete
from camel.messages import BaseMessage as BaseMessage
from pydantic import BaseModel
from typing import Any

class ChatAgentResponse(BaseModel):
    model_config: Incomplete
    msgs: list[BaseMessage]
    terminated: bool
    info: dict[str, Any]
    @property
    def msg(self): ...
