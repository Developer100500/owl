from _typeshed import Incomplete
from pydantic import BaseModel
from unstructured.documents.elements import Element

class Node(BaseModel):
    id: str | int
    type: str
    properties: dict

class Relationship(BaseModel):
    subj: Node
    obj: Node
    type: str
    timestamp: str | None
    properties: dict

class GraphElement(BaseModel):
    model_config: Incomplete
    nodes: list[Node]
    relationships: list[Relationship]
    source: Element
    def __post_init__(self) -> None: ...
