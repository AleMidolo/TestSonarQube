def tzname_in_python2(namefunc):
    """
    在 Python 2 中将 Unicode 输出转换为字节字符串

    在 Python 3 中，tzname() API 发生了变化。它曾经返回字节字符串，但在 Python 3 中被更改为返回 Unicode 字符串。
    """
    def convert_to_string(name):
        if name is None:
            return None
        if isinstance(name, str):
            return name
        if isinstance(name, unicode):
            return name.encode('ascii')
        return str(name)
    
    def wrapper(*args, **kwargs):
        result = namefunc(*args, **kwargs)
        if isinstance(result, tuple):
            return tuple(convert_to_string(n) for n in result)
        else:
            return convert_to_string(result)
            
    return wrapper