def strip_root(path, root):
    """
    Eliminar la raíz de la ruta, lanzar una excepción en caso de fallo.
    """
    if not path.startswith(root):
        raise ValueError("La ruta no comienza con la raíz proporcionada.")
    return path[len(root):]