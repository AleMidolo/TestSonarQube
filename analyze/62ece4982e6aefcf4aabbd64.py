def strip_root(path, root):
    """Remove root from path. If fails, throw exception
    
    Returns:
        A path without root
    """
    if not path.startswith(root):
        raise ValueError(f"Path '{path}' does not start with root '{root}'")
        
    # Remove root and any extra separators
    stripped = path[len(root):]
    while stripped.startswith('/'):
        stripped = stripped[1:]
        
    return stripped