def register_vcs_handler(vcs, method):  # decorador
    """Crear un decorador para marcar un método como el manejador de un VCS.

    Args:
        vcs: El nombre del sistema de control de versiones (VCS).
        method: El nombre del método que se utilizará como manejador.

    Returns:
        Un decorador que marca el método como el manejador del VCS especificado.
    """
    def decorate(f):
        f.vcs = vcs
        f.method = method
        return f
    return decorate