def is_run_el(obj):
    """
    El objeto contiene el método ejecutable 'run'.
    """
    return callable(getattr(obj, 'run', None))