def is_fill_compute_el(obj):
    """
    El objeto contiene los métodos ejecutables 'fill' y 'compute'.
    """
    return callable(getattr(obj, 'fill', None)) and callable(getattr(obj, 'compute', None))