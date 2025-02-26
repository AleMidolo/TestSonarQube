def strip_root(path, root):
    """
    Remove root from path. If fails, throw exception

    Returns:
        A path without root
    """
    if not path.startswith(root):
        raise ValueError("The path does not start with the specified root.")
    
    return path[len(root):]