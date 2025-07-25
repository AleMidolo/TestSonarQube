def strip_root(path, root):
    """   
    पथ से रूट को हटाएं, और यदि यह विफल होता है, तो अपवाद फेंकें।
    """
    if not path.startswith(root):
        raise ValueError(f"Path '{path}' does not start with root '{root}'")
        
    stripped = path[len(root):]
    
    # Remove leading slash if present
    if stripped.startswith('/') or stripped.startswith('\\'):
        stripped = stripped[1:]
        
    return stripped