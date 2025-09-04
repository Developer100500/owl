from _typeshed import Incomplete
from camel.agents import ChatAgent
from camel.messages import BaseMessage
from camel.models import BaseModelBackend as BaseModelBackend
from camel.responses import ChatAgentResponse
from camel.retrievers import VectorRetriever
from enum import Enum
from github.MainClass import Github
from pydantic import BaseModel

logger: Incomplete

class ProcessingMode(Enum):
    FULL_CONTEXT: Incomplete
    RAG: Incomplete

class GitHubFile(BaseModel):
    content: str
    file_path: str
    html_url: str

class RepositoryInfo(BaseModel):
    repo_name: str
    repo_url: str
    contents: list[GitHubFile]

class RepoAgent(ChatAgent):
    max_context_tokens: Incomplete
    vector_retriever: Incomplete
    github_auth_token: Incomplete
    chunk_size: Incomplete
    num_tokens: int
    processing_mode: Incomplete
    top_k: Incomplete
    similarity: Incomplete
    collection_name: Incomplete
    prompt_template: Incomplete
    full_text: str
    chunker: Incomplete
    repos: list[RepositoryInfo]
    def __init__(self, vector_retriever: VectorRetriever, system_message: str | None = 'You are a code assistant with repo context.', repo_paths: list[str] | None = None, model: BaseModelBackend | None = None, max_context_tokens: int = 2000, github_auth_token: str | None = None, chunk_size: int | None = 8192, top_k: int | None = 5, similarity: float | None = 0.6, collection_name: str | None = None, **kwargs) -> None: ...
    def parse_url(self, url: str) -> tuple[str, str]: ...
    def load_repositories(self, repo_urls: list[str]) -> list[RepositoryInfo]: ...
    def load_repository(self, repo_url: str, github_client: Github) -> RepositoryInfo: ...
    def count_tokens(self) -> int: ...
    def construct_full_text(self) -> None: ...
    def add_repositories(self, repo_urls: list[str]): ...
    def check_switch_mode(self) -> bool: ...
    def step(self, input_message: BaseMessage | str, *args, **kwargs) -> ChatAgentResponse: ...
    def reset(self) -> None: ...
    def search_by_file_path(self, file_path: str) -> str: ...
