from _typeshed import Incomplete
from camel.agents.chat_agent import ChatAgent
from camel.models import BaseModelBackend as BaseModelBackend

logger: Incomplete

class DeductiveReasonerAgent(ChatAgent):
    def __init__(self, model: BaseModelBackend | None = None) -> None: ...
    def deduce_conditions_and_quality(self, starting_state: str, target_state: str, role_descriptions_dict: dict[str, str] | None = None) -> dict[str, list[str] | dict[str, str]]: ...
