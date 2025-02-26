def is_fill_request_el(obj):
    """
    L'oggetto contiene i metodi eseguibili `fill` e `request`.
    """
    return hasattr(obj, 'fill') and callable(getattr(obj, 'fill')) and \
           hasattr(obj, 'request') and callable(getattr(obj, 'request'))