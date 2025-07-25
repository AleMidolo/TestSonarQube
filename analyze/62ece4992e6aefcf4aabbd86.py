def _dump_string(obj, dumper=None):
    """
    给定一个 Python 对象并将其序列化为 YAML 流

    参数：
        obj：Python 对象

    返回值：
        YAML 流

    将对象转储为 Python 2 的 Unicode 字符串或 Python 3 的字符串。
    """
    if isinstance(obj, str):
        return obj
    
    # Handle Python 2 unicode strings
    try:
        if isinstance(obj, unicode):
            return obj
    except NameError:
        pass
        
    # Convert other types to string
    try:
        return str(obj)
    except:
        return repr(obj)