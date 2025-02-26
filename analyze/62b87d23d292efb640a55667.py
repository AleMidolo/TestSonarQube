def register_vcs_handler(vcs, method):  # decorador
    """Crear un decorador para marcar un método como el manejador de un VCS.

    def decorate(f):
        """Función decoradora que registra el método como manejador."""
        if not hasattr(register_vcs_handler, 'handlers'):
            register_vcs_handler.handlers = {}
        register_vcs_handler.handlers[(vcs, method)] = f
        return f
    return decorate