def force_string(obj):
    """
    Esta función devuelve el objeto de tipo `bytes` correspondiente a ``obj`` en caso de que sea una cadena utilizando UTF-8.
    """
    if isinstance(obj, str):
        return obj.encode('utf-8')
    return obj