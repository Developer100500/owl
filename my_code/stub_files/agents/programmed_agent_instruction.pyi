import abc
from _typeshed import Incomplete
from camel.agents import ChatAgent
from camel.messages import BaseMessage
from enum import Enum
from pydantic import BaseModel
from typing import Any, Callable, Generic, TypeVar

T = TypeVar('T')

class ProgrammableAgentRequirement(Enum):
    LAST_MESSAGE_NOT_USER: str

class ProgrammedAgentInstructionResult(BaseModel, Generic[T]):
    user_message: BaseMessage
    agent_message: BaseMessage
    value: T
    model_config: Incomplete

class AbstractProgrammableAgent(abc.ABC):
    @abc.abstractmethod
    def run_atomic(self, callback: Callable[[], ProgrammedAgentInstructionResult[T]]) -> ProgrammedAgentInstructionResult[T]: ...
    @abc.abstractmethod
    def repair_state(self, requirement: ProgrammableAgentRequirement) -> None: ...

def programmable_capability(func: Callable[..., ProgrammedAgentInstructionResult[T]]) -> Callable[..., ProgrammedAgentInstructionResult[T]]: ...

class ProgrammableChatAgent(ChatAgent, AbstractProgrammableAgent):
    def __init__(self, **kwargs: Any) -> None: ...
    def run_atomic(self, callback: Callable[[], ProgrammedAgentInstructionResult[T]]) -> ProgrammedAgentInstructionResult[T]: ...
    def repair_state(self, requirement: ProgrammableAgentRequirement) -> None: ...
