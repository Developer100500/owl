from _typeshed import Incomplete
from camel.toolkits.base import BaseToolkit
from camel.toolkits.function_tool import FunctionTool

logger: Incomplete
DEFAULT_FORMAT: str

class FileWriteToolkit(BaseToolkit):
    output_dir: Incomplete
    default_encoding: Incomplete
    backup_enabled: Incomplete
    def __init__(self, output_dir: str = './', timeout: float | None = None, default_encoding: str = 'utf-8', backup_enabled: bool = True) -> None: ...
    def write_to_file(self, content: str | list[list[str]], filename: str, encoding: str | None = None) -> str: ...
    def get_tools(self) -> list[FunctionTool]: ...
