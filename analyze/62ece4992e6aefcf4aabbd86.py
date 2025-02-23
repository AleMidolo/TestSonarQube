def _dump_string(obj, dumper=None):
    """
    Volcar a una cadena en formato py2-unicode o py3-string
    """
    if dumper is None:
        dumper = str  # Default to str if no dumper is provided
    return dumper(obj)