def register_vcs_handler(vcs, method):  # decorator
    """Crea un decorator per contrassegnare un metodo come gestore di un VCS."""
    def decorator(f):
        # Store the VCS handler in the function's attributes
        if not hasattr(f, '_vcs_handlers'):
            f._vcs_handlers = {}
        f._vcs_handlers[vcs] = method
        return f
    return decorator