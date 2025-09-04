from _typeshed import Incomplete
from camel.models import BaseModelBackend as BaseModelBackend
from camel.toolkits.base import BaseToolkit
from camel.toolkits.function_tool import FunctionTool

logger: Incomplete

class OpenAIAgentToolkit(BaseToolkit):
    api_key: Incomplete
    client: Incomplete
    model: Incomplete
    def __init__(self, model: BaseModelBackend | None = None, api_key: str | None = None, timeout: float | None = None) -> None: ...
    def web_search(self, query: str) -> str: ...
    def file_search(self, query: str, vector_store_id: str) -> str: ...
    def get_tools(self) -> list[FunctionTool]: ...
