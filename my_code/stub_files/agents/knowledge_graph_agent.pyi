from _typeshed import Incomplete
from camel.agents import ChatAgent
from camel.models import BaseModelBackend as BaseModelBackend
from camel.storages.graph_storages.graph_element import GraphElement
from unstructured.documents.elements import Element

text_prompt: str

class KnowledgeGraphAgent(ChatAgent):
    def __init__(self, model: BaseModelBackend | None = None) -> None: ...
    element: Incomplete
    def run(self, element: Element, parse_graph_elements: bool = False, prompt: str | None = None) -> str | GraphElement: ...
