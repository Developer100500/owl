from pydantic import BaseModel
from typing import Callable

class WorkerConf(BaseModel):
    role: str
    sys_msg: str
    description: str

class TaskResult(BaseModel):
    content: str
    failed: bool

class TaskAssignResult(BaseModel):
    assignee_id: str

def check_if_running(running: bool) -> Callable: ...
