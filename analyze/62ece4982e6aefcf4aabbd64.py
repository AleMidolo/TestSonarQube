import os

def strip_root(path, root):
    """
    Remove root from path, throw exception on failure.

    Args:
        path (str): The full path from which to remove the root.
        root (str): The root path to be removed.

    Returns:
        str: A path without the root.

    Raises:
        ValueError: If the root is not found at the beginning of the path.
    """
    if not path.startswith(root):
        raise ValueError(f"Root '{root}' not found at the beginning of path '{path}'")
    
    stripped_path = path[len(root):]
    # Remove any leading slashes or backslashes
    stripped_path = stripped_path.lstrip(os.sep)
    return stripped_path