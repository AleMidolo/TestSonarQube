def _dump_string(obj, dumper=None):
    """
    पायथन 2 में यूनिकोड या पायथन 3 में स्ट्रिंग में डंप करें।
    """
    if isinstance(obj, str):
        return obj
    elif hasattr(obj, 'encode'):
        return obj.encode('utf-8')
    else:
        return str(obj)