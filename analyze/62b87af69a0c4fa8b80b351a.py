def is_fill_compute_el(obj):
    """
    El objeto contiene los métodos ejecutables 'fill' y 'compute'.
    """
    return all(callable(getattr(obj, method, None)) for method in ['fill', 'compute'])