from _typeshed import Incomplete
from camel.extractors.base import BaseExtractor as BaseExtractor
from camel.verifiers import BaseVerifier

logger: Incomplete

class PythonVerifier(BaseVerifier):
    venv_path: str | None
    required_packages: Incomplete
    float_tolerance: Incomplete
    bin_dir: str
    def __init__(self, extractor: BaseExtractor | None = None, timeout: float | None = 30.0, required_packages: list[str] | None = None, float_tolerance: float | None = None, **kwargs) -> None: ...
