def register_vcs_handler(vcs, method):  # decorador
    """Crear un decorador para marcar un método como el manejador de un VCS.

    Args:
        vcs: El sistema de control de versiones (VCS) que se manejará.
        method: El método que se utilizará para manejar el VCS.

    Returns:
        Un decorador que marca el método como el manejador del VCS especificado.
    """
    def decorate(f):
        f.vcs = vcs
        f.method = method
        return f
    return decorate