from camel.toolkits import FunctionTool as FunctionTool
from camel.utils import AgentOpsMeta
from mcp.server import FastMCP

class BaseToolkit(metaclass=AgentOpsMeta):
    mcp: FastMCP
    timeout: float | None
    def __init__(self, timeout: float | None = None) -> None: ...
    def __init_subclass__(cls, **kwargs) -> None: ...
    def get_tools(self) -> list[FunctionTool]: ...
