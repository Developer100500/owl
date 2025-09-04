from _typeshed import Incomplete
from camel.toolkits.base import BaseToolkit
from camel.toolkits.function_tool import FunctionTool

logger: Incomplete

class ExcelToolkit(BaseToolkit):
    def __init__(self, timeout: float | None = None) -> None: ...
    def extract_excel_content(self, document_path: str) -> str: ...
    def get_tools(self) -> list[FunctionTool]: ...
