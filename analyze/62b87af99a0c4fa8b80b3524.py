def is_run_el(obj):
    """
     Controlla se l'oggetto contiene il metodo eseguibile 'run'.
    """
    return callable(getattr(obj, 'run', None))