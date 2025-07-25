def is_fill_compute_el(obj):
    """
    Object contains executable methods 'fill' and 'compute'.
    """
    return all(callable(getattr(obj, method, None)) for method in ['fill', 'compute'])