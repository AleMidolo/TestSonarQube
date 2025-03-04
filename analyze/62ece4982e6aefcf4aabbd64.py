def strip_root(path, root):
    """Remove root from path. If fails, throw exception
    
    Returns:
        A path without root
    """
    if not path.startswith(root):
        raise ValueError(f"Path '{path}' does not start with root '{root}'")
        
    return path[len(root):].lstrip('/')