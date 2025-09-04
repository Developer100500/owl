from .models import VerificationResult
from .python_verifier import PythonVerifier
from _typeshed import Incomplete
from camel.extractors.base import BaseExtractor as BaseExtractor
from typing import Any

logger: Incomplete

class UnitParser:
    allowed_units: Incomplete
    def __init__(self) -> None: ...
    def parse_unit(self, unit_str: str) -> Any | None: ...
    def parse_unit_with_latex(self, unit_str: str) -> Any: ...
    def detect_scaling_factor(self, unit_expr: Any) -> tuple[int | float | Any, Any]: ...
    @staticmethod
    def preprocess_unit_string(unit_str: str) -> str: ...
    @staticmethod
    def unit_is_none(unit_str: str | None) -> bool: ...
    @staticmethod
    def extract_value_and_unit(expr: Any) -> tuple[int | float | Any, Any]: ...
    @staticmethod
    def detect_unit_args(unit_expr: Any) -> list[Any]: ...

class PhysicsSolutionComparator:
    solution: str
    reference_answer: str
    tolerance: Incomplete
    unit_parser: UnitParser
    gt_value: Any
    gt_unit: str
    sol_value: Any
    sol_unit: str
    gt_unit_expr: Any
    sol_unit_expr: Any
    def __init__(self, solution: str, reference_answer: str, float_tolerance: float | None = None) -> None: ...
    @staticmethod
    def verify_unit(sol_unit_expr: Any, gt_unit_expr: Any) -> bool: ...
    def compare_solution_to_reference(self) -> VerificationResult: ...

class PhysicsVerifier(PythonVerifier):
    tolerance: Incomplete
    def __init__(self, extractor: BaseExtractor | None = None, timeout: float | None = 30.0, required_packages: list[str] | None = None, float_tolerance: float | None = None, **kwargs) -> None: ...
