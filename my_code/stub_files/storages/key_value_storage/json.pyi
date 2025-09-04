import json
from _typeshed import Incomplete
from camel.storages.key_value_storages import BaseKeyValueStorage
from enum import EnumMeta as EnumMeta
from pathlib import Path
from typing import Any, ClassVar

class CamelJSONEncoder(json.JSONEncoder):
    CAMEL_ENUMS: ClassVar[dict[str, EnumMeta]]
    def default(self, obj) -> Any: ...

class JsonStorage(BaseKeyValueStorage):
    json_path: Incomplete
    def __init__(self, path: Path | None = None) -> None: ...
    def save(self, records: list[dict[str, Any]]) -> None: ...
    def load(self) -> list[dict[str, Any]]: ...
    def clear(self) -> None: ...
