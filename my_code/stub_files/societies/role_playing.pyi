import threading
from _typeshed import Incomplete
from camel.agents import ChatAgent, CriticAgent
from camel.human import Human
from camel.messages import BaseMessage
from camel.models import BaseModelBackend as BaseModelBackend
from camel.prompts import TextPrompt as TextPrompt
from camel.responses import ChatAgentResponse
from camel.types import TaskType

logger: Incomplete

class RolePlaying:
    with_task_specify: Incomplete
    with_task_planner: Incomplete
    with_critic_in_the_loop: Incomplete
    model: Incomplete
    task_type: Incomplete
    task_prompt: Incomplete
    specified_task_prompt: TextPrompt | None
    planned_task_prompt: TextPrompt | None
    assistant_agent: ChatAgent
    user_agent: ChatAgent
    assistant_sys_msg: BaseMessage | None
    user_sys_msg: BaseMessage | None
    critic: CriticAgent | Human | None
    critic_sys_msg: BaseMessage | None
    def __init__(self, assistant_role_name: str, user_role_name: str, *, critic_role_name: str = 'critic', task_prompt: str = '', with_task_specify: bool = True, with_task_planner: bool = False, with_critic_in_the_loop: bool = False, critic_criteria: str | None = None, model: BaseModelBackend | None = None, task_type: TaskType = ..., assistant_agent_kwargs: dict | None = None, user_agent_kwargs: dict | None = None, task_specify_agent_kwargs: dict | None = None, task_planner_agent_kwargs: dict | None = None, critic_kwargs: dict | None = None, sys_msg_generator_kwargs: dict | None = None, extend_sys_msg_meta_dicts: list[dict] | None = None, extend_task_specify_meta_dict: dict | None = None, output_language: str | None = None, stop_event: threading.Event | None = None) -> None: ...
    def init_chat(self, init_msg_content: str | None = None) -> BaseMessage: ...
    async def ainit_chat(self, init_msg_content: str | None = None) -> BaseMessage: ...
    def step(self, assistant_msg: BaseMessage) -> tuple[ChatAgentResponse, ChatAgentResponse]: ...
    async def astep(self, assistant_msg: BaseMessage) -> tuple[ChatAgentResponse, ChatAgentResponse]: ...
