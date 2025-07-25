def _dump_string(obj, dumper=None):
    """
    पायथन 2 में यूनिकोड या पायथन 3 में स्ट्रिंग में डंप करें।
    """
    if dumper is None:
        dumper = str  # Default dumper to str if not provided

    if isinstance(obj, str):
        return dumper(obj)
    elif isinstance(obj, bytes):
        return dumper(obj.decode('utf-8'))
    else:
        raise TypeError("Expected a string or bytes object")