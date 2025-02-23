def registra_gestore_vcs(vcs, metodo):  # decorator
    """Crea un decorator per contrassegnare un metodo come gestore di un VCS."""
    
    def decorator(func):
        func.vcs = vcs
        func.metodo = metodo
        return func
    
    return decorator