from .models import Action, Observation
from _typeshed import Incomplete
from camel.datasets import BaseGenerator, StaticDataset
from camel.verifiers.base import BaseVerifier
from typing import Any

logger: Incomplete

class SingleStepEnv:
    PLACEHOLDER_OBS: Incomplete
    ACCURACY_REWARD: int
    dataset: Incomplete
    verifier: Incomplete
    current_batch_size: int
    def __init__(self, dataset: StaticDataset | BaseGenerator, verifier: BaseVerifier, timeout: float | None = 180.0, **kwargs) -> None: ...
    async def setup(self) -> None: ...
    async def close(self) -> None: ...
    async def reset(self, batch_size: int = 1, seed: int | None = None) -> Observation | list[Observation]: ...
    async def step(self, action: Action | list[Action] | str | dict[int, str]) -> tuple[Observation, float, bool, dict[str, Any]] | list[tuple[Observation, float, bool, dict[str, Any]]]: ...
    @property
    def metadata(self) -> dict[str, Any]: ...
