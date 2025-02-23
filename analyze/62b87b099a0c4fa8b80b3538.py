def is_fill_request_el(obj):
    """
    L'oggetto contiene i metodi eseguibili `fill` e `request`.
    """
    return callable(getattr(obj, 'fill', None)) and callable(getattr(obj, 'request', None))