def _dump_string(obj, dumper=None):
    """
    Dump to a py2-unicode or py3-string
    """
    if dumper is None:
        dumper = str  # Default to str if no dumper is provided

    if isinstance(obj, str):
        return dumper(obj)
    elif isinstance(obj, bytes):
        return dumper(obj.decode('utf-8', errors='replace'))
    else:
        return dumper(str(obj))