def is_fill_request_el(obj):
    """
    L'oggetto contiene i metodi eseguibili `fill` e `request`.
    """
    return all(callable(getattr(obj, method, None)) for method in ['fill', 'request'])