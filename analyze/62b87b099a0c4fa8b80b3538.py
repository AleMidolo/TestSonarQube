def is_fill_request_el(obj):
    """
    `Object` में निष्पादन योग्य मेथड्स `fill` और `request` मौजूद हैं।
    """
    return all(callable(getattr(obj, method, None)) for method in ['fill', 'request'])