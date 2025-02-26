def force_string(obj):
    """
    Questa funzione restituisce l'oggetto di tipo `bytes` corrispondente a ``obj`` nel caso in cui sia una stringa utilizzando UTF-8.
    """
    if isinstance(obj, str):
        return obj.encode('utf-8')
    return obj