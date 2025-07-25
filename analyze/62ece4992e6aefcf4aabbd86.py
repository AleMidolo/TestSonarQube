def _dump_string(obj, dumper=None):
    """
    Serializza in una stringa Unicode (Python 2) o in una stringa (Python 3).
    """
    if isinstance(obj, str):
        return obj
    elif isinstance(obj, bytes):
        return obj.decode('utf-8')
    else:
        raise TypeError("Expected a string or bytes, got {}".format(type(obj)))