from _typeshed import Incomplete
from camel.agents.chat_agent import ChatAgent
from camel.memories import AgentMemory as AgentMemory
from camel.messages import BaseMessage
from camel.models import BaseModelBackend as BaseModelBackend
from camel.responses import ChatAgentResponse
from typing import Any, Sequence

class CriticAgent(ChatAgent):
    options_dict: dict[str, str]
    retry_attempts: Incomplete
    verbose: Incomplete
    logger_color: Incomplete
    def __init__(self, system_message: BaseMessage, model: BaseModelBackend | None = None, memory: AgentMemory | None = None, message_window_size: int = 6, retry_attempts: int = 2, verbose: bool = False, logger_color: Any = ...) -> None: ...
    def flatten_options(self, messages: Sequence[BaseMessage]) -> str: ...
    def get_option(self, input_message: BaseMessage) -> str: ...
    def parse_critic(self, critic_msg: BaseMessage) -> str | None: ...
    def reduce_step(self, input_messages: Sequence[BaseMessage]) -> ChatAgentResponse: ...
