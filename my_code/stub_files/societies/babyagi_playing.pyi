from _typeshed import Incomplete
from camel.agents import ChatAgent, TaskCreationAgent, TaskPrioritizationAgent
from camel.agents.chat_agent import ChatAgentResponse
from camel.messages import BaseMessage
from camel.prompts import TextPrompt
from camel.types import TaskType
from collections import deque

logger: Incomplete

class BabyAGI:
    task_type: Incomplete
    task_prompt: Incomplete
    specified_task_prompt: TextPrompt
    assistant_agent: ChatAgent
    assistant_sys_msg: BaseMessage | None
    task_creation_agent: TaskCreationAgent
    task_prioritization_agent: TaskPrioritizationAgent
    subtasks: deque
    solved_subtasks: list[str]
    MAX_TASK_HISTORY: Incomplete
    def __init__(self, assistant_role_name: str, user_role_name: str, task_prompt: str = '', task_type: TaskType = ..., max_task_history: int = 10, assistant_agent_kwargs: dict | None = None, task_specify_agent_kwargs: dict | None = None, task_creation_agent_kwargs: dict | None = None, task_prioritization_agent_kwargs: dict | None = None, sys_msg_generator_kwargs: dict | None = None, extend_task_specify_meta_dict: dict | None = None, output_language: str | None = None, message_window_size: int | None = None) -> None: ...
    def init_specified_task_prompt(self, assistant_role_name: str, user_role_name: str, task_specify_agent_kwargs: dict | None, extend_task_specify_meta_dict: dict | None, output_language: str | None): ...
    def init_agents(self, init_assistant_sys_msg: BaseMessage, assistant_agent_kwargs: dict | None, task_creation_agent_kwargs: dict | None, task_prioritization_agent_kwargs: dict | None, output_language: str | None, message_window_size: int | None = None): ...
    def step(self) -> ChatAgentResponse: ...
