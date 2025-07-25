def _dump_string(obj, dumper=None):
    """
    Dump to a py2-unicode or py3-string
    """
    if dumper is not None:
        return dumper(obj)
    if isinstance(obj, bytes):
        return obj.decode('utf-8')
    return str(obj)