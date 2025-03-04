def register_vcs_handler(vcs, method):  # decorator
    """Crea un decorator per contrassegnare un metodo come gestore di un VCS."""
    def decorator(func):
        func.vcs = vcs
        func.method = method
        return func
    return decorator