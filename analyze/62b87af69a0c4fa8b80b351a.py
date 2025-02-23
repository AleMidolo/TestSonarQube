def is_fill_compute_el(obj):
    """
    Verifica se l'oggetto contiene i metodi eseguibili 'fill' e 'compute'.
    """
    return callable(getattr(obj, 'fill', None)) and callable(getattr(obj, 'compute', None))