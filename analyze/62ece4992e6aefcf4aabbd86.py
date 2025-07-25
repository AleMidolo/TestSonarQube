def _dump_string(obj, dumper=None):
    """
    Serializza in una stringa Unicode (Python 2) o in una stringa (Python 3).
    """
    if dumper is not None:
        return dumper(obj)
    else:
        return str(obj)