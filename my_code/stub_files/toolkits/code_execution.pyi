from _typeshed import Incomplete
from camel.interpreters import DockerInterpreter, E2BInterpreter, InternalPythonInterpreter, JupyterKernelInterpreter, SubprocessInterpreter
from camel.toolkits import FunctionTool
from camel.toolkits.base import BaseToolkit
from typing import Literal

class CodeExecutionToolkit(BaseToolkit):
    verbose: Incomplete
    unsafe_mode: Incomplete
    import_white_list: Incomplete
    interpreter: InternalPythonInterpreter | JupyterKernelInterpreter | DockerInterpreter | SubprocessInterpreter | E2BInterpreter
    def __init__(self, sandbox: Literal['internal_python', 'jupyter', 'docker', 'subprocess', 'e2b'] = 'subprocess', verbose: bool = False, unsafe_mode: bool = False, import_white_list: list[str] | None = None, require_confirm: bool = False, timeout: float | None = None) -> None: ...
    def execute_code(self, code: str) -> str: ...
    def get_tools(self) -> list[FunctionTool]: ...
