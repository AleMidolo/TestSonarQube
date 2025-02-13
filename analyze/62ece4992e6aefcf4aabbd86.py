def _dump_string(obj, dumper=None):
    """
    Serializza in una stringa Unicode (Python 2) o in una stringa (Python 3).
    """
    if isinstance(obj, str):
        return obj
    elif isinstance(obj, bytes):
        return obj.decode('utf-8')
    elif dumper is not None:
        return dumper(obj)
    else:
        raise TypeError("Object of type '{}' is not serializable".format(type(obj).__name__))