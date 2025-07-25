def is_fill_request_el(obj):
    """
    Object contains executable methods 'fill' and 'request'.
    """
    return all(callable(getattr(obj, method, None)) for method in ['fill', 'request'])