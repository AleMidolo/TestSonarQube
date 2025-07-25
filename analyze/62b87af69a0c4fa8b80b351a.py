def is_fill_compute_el(obj):
    """
    Object contains executable methods 'fill' and 'compute'.
    """
    return callable(getattr(obj, 'fill', None)) and callable(getattr(obj, 'compute', None))