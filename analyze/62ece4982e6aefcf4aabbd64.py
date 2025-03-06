import os

def strip_root(path, root):
    """
    Remove root from path. If fails, throw exception.

    Args:
        path (str): The full path from which to remove the root.
        root (str): The root part of the path to be removed.

    Returns:
        str: A path without the root.

    Raises:
        ValueError: If the root is not found at the beginning of the path.
    """
    if not path.startswith(root):
        raise ValueError(f"The path '{path}' does not start with the root '{root}'.")
    
    stripped_path = path[len(root):]
    return stripped_path