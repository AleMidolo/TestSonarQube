def _dump_string(obj, dumper=None):
    """
    Volcar a una cadena en formato py2-unicode o py3-string
    """
    if dumper is not None:
        return dumper(obj)
    if isinstance(obj, str):
        return obj
    elif isinstance(obj, bytes):
        return obj.decode('utf-8')
    else:
        return str(obj)