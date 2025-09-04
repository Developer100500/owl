from _typeshed import Incomplete
from camel.agents import ChatAgent
from camel.societies.workforce.worker import Worker
from typing import Any

class SingleAgentWorker(Worker):
    worker: Incomplete
    def __init__(self, description: str, worker: ChatAgent) -> None: ...
    def reset(self) -> Any: ...
