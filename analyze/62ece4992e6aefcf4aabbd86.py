def _dump_string(obj, dumper=None):
    """
    Serializza in una stringa Unicode (Python 2) o in una stringa (Python 3).
    """
    if isinstance(obj, str):
        return obj
    elif isinstance(obj, bytes):
        return obj.decode('utf-8')
    elif isinstance(obj, unicode):  # For Python 2 compatibility
        return obj.encode('utf-8')
    else:
        raise TypeError("Object must be a string or bytes")