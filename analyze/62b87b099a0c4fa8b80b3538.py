def is_fill_request_el(obj):
    """
    El objeto contiene métodos ejecutables `fill` y `request`.
    """
    return callable(getattr(obj, 'fill', None)) and callable(getattr(obj, 'request', None))