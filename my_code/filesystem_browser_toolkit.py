import os
from camel.toolkits import FunctionTool
from typing import Optional, List

def get_files(folder_path: Optional[str] = None, recursive: bool = False) -> List[str]:
    """
    Returns a list of all files in the specified folder or current directory.
    
    Args:
        folder_path (Optional[str], optional): Path to the folder to search. 
            If None, uses current directory.
        recursive (bool, optional): If True, searches for files in all 
            subdirectories. Defaults to False.
    
    Returns:
        List[str]: A list of file paths.
    """
    if folder_path is None:
        target_dir = os.getcwd()
    else:
        target_dir = folder_path
    
    files = []
    
    if recursive:
        for root, _, filenames in os.walk(target_dir):
            for filename in filenames:
                files.append(os.path.join(root, filename))
    else:
        for item in os.listdir(target_dir):
            item_path = os.path.join(target_dir, item)
            if os.path.isfile(item_path):
                files.append(item_path)
    
    return files

def is_folder(path: str) -> bool:
    """
    Check if the given path is a directory.
    
    Args:
        path (str): Path to check
    
    Returns:
        bool: True if path is a directory, False otherwise
    """
    return os.path.isdir(path)

def is_file(path: str) -> bool:
    """
    Check if the given path is a file.
    
    Args:
        path (str): Path to check
    
    Returns:
        bool: True if path is a file, False otherwise
    """
    return os.path.isfile(path)

get_files_tool = FunctionTool(get_files)
is_folder_tool = FunctionTool(is_folder)
is_file_tool = FunctionTool(is_file)