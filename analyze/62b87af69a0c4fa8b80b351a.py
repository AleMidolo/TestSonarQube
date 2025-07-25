def is_fill_compute_el(obj):
    """
    El objeto contiene los métodos ejecutables 'fill' y 'compute'.
    """
    return hasattr(obj, 'fill') and callable(getattr(obj, 'fill')) and \
           hasattr(obj, 'compute') and callable(getattr(obj, 'compute'))