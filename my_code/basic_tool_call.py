from camel.societies.workforce import Workforce
from camel.models import ModelFactory
from camel.types import ModelPlatformType, ModelType
from camel.agents import ChatAgent
from camel.tasks import Task

from camel.prompts import PromptTemplateGenerator
from camel.types import TaskType
from dotenv import load_dotenv
import pathlib
import sys

# Add the script's directory to the Python path to resolve local imports
script_dir = pathlib.Path(__file__).parent.resolve()
if str(script_dir) not in sys.path:
    sys.path.append(str(script_dir))

from filesystem_browser_toolkit import get_files_tool, is_file_tool, is_folder_tool

base_dir = pathlib.Path(__file__).parent.parent
env_path = base_dir / "owl" / ".env"
load_dotenv(dotenv_path=str(env_path))

import os



model = ModelFactory.create(
    url="https://api.vsegpt.ru/v1",
    model_platform=ModelPlatformType.OPENAI,
    model_type="openai/gpt-5-mini",
    model_config_dict={"temperature": 0.1, "max_tokens": 5000}
)

files_searcher_agent = ChatAgent(
    model=model,
    system_message="You are a helpful assistant that can search files on computer. You can use tools to browse and find requested files.",
    tools=[get_files_tool, is_file_tool, is_folder_tool]
)

workforce = Workforce(
    description="My File System Search Workforce",
    children=[files_searcher_agent],
    new_worker_agent_kwargs={"model": model},
    task_agent_kwargs={"model": model},
    coordinator_agent_kwargs={"model": model}
)

def main():
    workforce.add_single_agent_worker(
        description="A worker that can search files on computer.",
        worker=files_searcher_agent
    )

    task = Task(
        content="Find the file named 'find_me.txt'. It can be in the current directory or any subdirectory. Use recursive search.",
        id="0",
    )

    print(task.content)

    output = files_searcher_agent.step(
        input_message=task.content
    )

    print(output)

    """ resp = workforce.process_task(
        task=task
    ) """
    #print(resp)


if __name__ == "__main__":
    main()