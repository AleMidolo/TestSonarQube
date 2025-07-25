def register_vcs_handler(vcs, method):  # decorador
    """Crear un decorador para marcar un método como el manejador de un VCS.

    Args:
        vcs (str): El nombre del sistema de control de versiones (VCS).
        method (str): El nombre del método que se usará como manejador.

    Returns:
        function: El decorador que marca el método como manejador del VCS.
    """
    def decorate(f):
        f.vcs = vcs
        f.method = method
        return f
    return decorate