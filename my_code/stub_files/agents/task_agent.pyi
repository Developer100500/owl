from _typeshed import Incomplete
from camel.agents.chat_agent import ChatAgent
from camel.models import BaseModelBackend as BaseModelBackend
from camel.prompts import TextPrompt
from camel.types import TaskType
from typing import Any

class TaskSpecifyAgent(ChatAgent):
    DEFAULT_WORD_LIMIT: int
    task_specify_prompt: str | TextPrompt
    def __init__(self, model: BaseModelBackend | None = None, task_type: TaskType = ..., task_specify_prompt: str | TextPrompt | None = None, word_limit: int = ..., output_language: str | None = None) -> None: ...
    def run(self, task_prompt: str | TextPrompt, meta_dict: dict[str, Any] | None = None) -> TextPrompt: ...

class TaskPlannerAgent(ChatAgent):
    task_planner_prompt: Incomplete
    def __init__(self, model: BaseModelBackend | None = None, output_language: str | None = None) -> None: ...
    def run(self, task_prompt: str | TextPrompt) -> TextPrompt: ...

class TaskCreationAgent(ChatAgent):
    task_creation_prompt: Incomplete
    objective: Incomplete
    def __init__(self, role_name: str, objective: str | TextPrompt, model: BaseModelBackend | None = None, output_language: str | None = None, message_window_size: int | None = None, max_task_num: int | None = 3) -> None: ...
    def run(self, task_list: list[str]) -> list[str]: ...

class TaskPrioritizationAgent(ChatAgent):
    task_prioritization_prompt: Incomplete
    objective: Incomplete
    def __init__(self, objective: str | TextPrompt, model: BaseModelBackend | None = None, output_language: str | None = None, message_window_size: int | None = None) -> None: ...
    def run(self, task_list: list[str]) -> list[str]: ...
