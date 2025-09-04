from _typeshed import Incomplete
from camel.agents.chat_agent import ChatAgent
from camel.agents.tool_agents.base import BaseToolAgent as BaseToolAgent
from camel.interpreters import BaseInterpreter
from camel.messages import BaseMessage
from camel.models import BaseModelBackend as BaseModelBackend
from camel.responses import ChatAgentResponse
from typing import Any

class EmbodiedAgent(ChatAgent):
    tool_agents: Incomplete
    code_interpreter: BaseInterpreter
    verbose: Incomplete
    logger_color: Incomplete
    def __init__(self, system_message: BaseMessage, model: BaseModelBackend | None = None, message_window_size: int | None = None, tool_agents: list[BaseToolAgent] | None = None, code_interpreter: BaseInterpreter | None = None, verbose: bool = False, logger_color: Any = ...) -> None: ...
    def get_tool_agent_names(self) -> list[str]: ...
    def step(self, input_message: BaseMessage) -> ChatAgentResponse: ...
