def register_vcs_handler(vcs, method):  # decorator
    """Crea un decorator per contrassegnare un metodo come gestore di un VCS."""
    def decorator(func):
        func.vcs_handler = True
        func.vcs_type = vcs
        func.method_type = method
        return func
    return decorator