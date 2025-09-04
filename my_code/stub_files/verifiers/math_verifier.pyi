from _typeshed import Incomplete
from camel.extractors.base import BaseExtractor as BaseExtractor
from camel.verifiers import BaseVerifier

logger: Incomplete

class MathVerifier(BaseVerifier):
    float_rounding: Incomplete
    numeric_precision: Incomplete
    enable_wrapping: Incomplete
    def __init__(self, extractor: BaseExtractor | None = None, timeout: float | None = 30.0, float_rounding: int = 6, numeric_precision: int = 15, enable_wrapping: bool | None = False, **kwargs) -> None: ...
