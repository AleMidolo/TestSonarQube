def is_fill_compute_el(obj):
    """
    Object contains executable methods 'fill' and 'compute'.
    """
    return hasattr(obj, 'fill') and callable(getattr(obj, 'fill')) and \
           hasattr(obj, 'compute') and callable(getattr(obj, 'compute'))