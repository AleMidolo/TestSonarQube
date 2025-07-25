def registra_gestore_vcs(vcs, metodo):  # decorator
    """Crea un decorator per contrassegnare un metodo come gestore di un VCS."""
    def decorator(func):
        if not hasattr(func, '_vcs_gestori'):
            func._vcs_gestori = {}
        func._vcs_gestori[vcs] = metodo
        return func
    return decorator