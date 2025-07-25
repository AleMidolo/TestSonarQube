def _dump_string(obj, dumper=None):
    """
    पायथन 2 में यूनिकोड या पायथन 3 में स्ट्रिंग में डंप करें।
    """
    if isinstance(obj, str):
        return obj
    elif isinstance(obj, bytes):
        return obj.decode('utf-8')
    elif isinstance(obj, unicode):  # For Python 2 compatibility
        return obj.encode('utf-8')
    else:
        raise TypeError("Expected a string or bytes object, got: {}".format(type(obj)))