def _dump_string(obj, dumper=None):
    """
    पायथन 2 में यूनिकोड या पायथन 3 में स्ट्रिंग में डंप करें।
    """
    if dumper is not None:
        return dumper(obj)
    if isinstance(obj, str):
        return obj
    if isinstance(obj, bytes):
        return obj.decode('utf-8')
    return str(obj)