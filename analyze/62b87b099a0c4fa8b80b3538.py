def is_fill_request_el(obj):
    """
    `Object` में निष्पादन योग्य मेथड्स `fill` और `request` मौजूद हैं।
    """
    return callable(getattr(obj, 'fill', None)) and callable(getattr(obj, 'request', None))