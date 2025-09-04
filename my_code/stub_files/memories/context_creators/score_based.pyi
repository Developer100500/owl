from _typeshed import Incomplete
from camel.memories.base import BaseContextCreator
from camel.memories.records import ContextRecord
from camel.messages import OpenAIMessage as OpenAIMessage
from camel.utils import BaseTokenCounter
from pydantic import BaseModel

logger: Incomplete

class _ContextUnit(BaseModel):
    idx: int
    record: ContextRecord
    num_tokens: int

class ScoreBasedContextCreator(BaseContextCreator):
    def __init__(self, token_counter: BaseTokenCounter, token_limit: int) -> None: ...
    @property
    def token_counter(self) -> BaseTokenCounter: ...
    @property
    def token_limit(self) -> int: ...
    def create_context(self, records: list[ContextRecord]) -> tuple[list[OpenAIMessage], int]: ...
