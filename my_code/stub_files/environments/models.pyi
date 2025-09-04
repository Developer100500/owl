from datetime import datetime
from pydantic import BaseModel
from typing import Any, Protocol

class Action(BaseModel):
    index: int
    llm_response: str
    metadata: dict[str, Any]
    timestamp: datetime

class Observation(BaseModel):
    question: str
    context: dict[str, Any]
    metadata: dict[str, Any] | None

class StepResult(BaseModel):
    observation: Observation
    reward: float
    rewards_dict: dict[str, float]
    done: bool
    info: dict[str, Any]
    def as_tuple(self) -> tuple[Observation, float, bool, dict[str, Any]]: ...

class Environment(Protocol):
    async def reset(self) -> Observation: ...
    async def step(self, action: Action) -> StepResult: ...
    async def close(self) -> None: ...
