def strip_root(path, root):
    """
    Eliminar la raíz de la ruta, lanzar una excepción en caso de fallo.
    """
    if not path.startswith(root):
        raise ValueError(f"Path '{path}' does not start with root '{root}'")
    
    # Remove root from path and any leading slashes
    stripped = path[len(root):].lstrip('/')
    
    return stripped