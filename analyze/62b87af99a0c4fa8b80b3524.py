def is_run_el(obj):
    """
     Controlla se l'oggetto contiene il metodo eseguibile 'run'.
    """
    return hasattr(obj, 'run') and callable(getattr(obj, 'run'))