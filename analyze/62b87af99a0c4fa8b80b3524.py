def is_run_el(obj):
    """
    El objeto contiene el método ejecutable 'run'.
    """
    return hasattr(obj, 'run') and callable(getattr(obj, 'run'))