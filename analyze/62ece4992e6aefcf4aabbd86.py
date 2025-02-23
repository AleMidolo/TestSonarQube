def _dump_string(obj, dumper=None):
    """
    Dump to a py2-unicode or py3-string
    """
    if dumper is None:
        dumper = str  # Default to str if no dumper is provided
    return dumper(obj)