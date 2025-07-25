def strip_root(path, root):
    """
    Remove root from path, throw exception on failure.

    Args:
        path (str): The full path.
        root (str): The root part of the path to be removed.

    Returns:
        str: A path without the root.

    Raises:
        ValueError: If the root is not found at the beginning of the path.
    """
    if not path.startswith(root):
        raise ValueError(f"Root '{root}' not found at the beginning of path '{path}'")
    return path[len(root):]