from _typeshed import Incomplete
from camel.retrievers import AutoRetriever
from camel.toolkits import FunctionTool
from camel.toolkits.base import BaseToolkit

class RetrievalToolkit(BaseToolkit):
    ar: Incomplete
    def __init__(self, auto_retriever: AutoRetriever | None = None, timeout: float | None = None) -> None: ...
    def information_retrieval(self, query: str, contents: str | list[str], top_k: int = ..., similarity_threshold: float = ...) -> str: ...
    def get_tools(self) -> list[FunctionTool]: ...
