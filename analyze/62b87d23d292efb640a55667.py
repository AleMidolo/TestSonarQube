def register_vcs_handler(vcs, method):  # decorator
    """Crea un decorator per contrassegnare un metodo come gestore di un VCS."""
    def decorator(func):
        if not hasattr(func, '_vcs_handlers'):
            func._vcs_handlers = {}
        func._vcs_handlers[vcs] = method
        return func
    return decorator