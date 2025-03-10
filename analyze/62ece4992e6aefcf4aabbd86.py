def _dump_string(obj, dumper=None):
    """
    Dump to a py2-unicode or py3-string
    """
    if dumper is not None:
        return dumper(obj)
    else:
        return str(obj)