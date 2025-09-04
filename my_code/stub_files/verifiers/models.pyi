from datetime import datetime
from enum import Enum
from pydantic import BaseModel
from typing import Any

class VerificationOutcome(Enum):
    SUCCESS: str
    FAILURE: str
    ERROR: str
    TIMEOUT: str
    def __bool__(self) -> bool: ...

class VerificationResult(BaseModel):
    status: VerificationOutcome
    result: str
    duration: float
    timestamp: datetime
    metadata: dict[str, Any]
    error_message: str | None

class VerifierConfig(BaseModel):
    enabled: bool
    strict_mode: bool
    timeout: float | None
    max_retries: int
    retry_delay: float
