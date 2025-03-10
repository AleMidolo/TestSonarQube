def strip_root(path, root):
    """
    Eliminar la raíz de la ruta, lanzar una excepción en caso de fallo.
    """
    if not path.startswith(root):
        raise ValueError(f"La ruta '{path}' no comienza con la raíz '{root}'")
    return path[len(root):]