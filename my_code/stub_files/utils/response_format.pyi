from _typeshed import Incomplete
from pydantic import BaseModel
from typing import Any, Callable

def get_pydantic_model(input_data: str | type[BaseModel] | Callable) -> type[BaseModel]: ...

TYPE_MAPPING: Incomplete

def model_from_json_schema(name: str, schema: dict[str, Any]) -> type[BaseModel]: ...
