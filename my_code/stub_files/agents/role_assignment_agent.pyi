from camel.agents.chat_agent import ChatAgent
from camel.models import BaseModelBackend as BaseModelBackend
from camel.prompts import TextPrompt

class RoleAssignmentAgent(ChatAgent):
    def __init__(self, model: BaseModelBackend | None = None) -> None: ...
    def run(self, task_prompt: str | TextPrompt, num_roles: int = 2) -> dict[str, str]: ...
