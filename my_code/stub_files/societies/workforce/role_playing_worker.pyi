from _typeshed import Incomplete
from camel.societies.workforce.worker import Worker

class RolePlayingWorker(Worker):
    summarize_agent: Incomplete
    chat_turn_limit: Incomplete
    assistant_role_name: Incomplete
    user_role_name: Incomplete
    assistant_agent_kwargs: Incomplete
    user_agent_kwargs: Incomplete
    def __init__(self, description: str, assistant_role_name: str, user_role_name: str, assistant_agent_kwargs: dict | None = None, user_agent_kwargs: dict | None = None, chat_turn_limit: int = 3) -> None: ...
