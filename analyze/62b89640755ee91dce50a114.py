def tzname_in_python2(namefunc):
    """
    在 Python 2 中将 Unicode 输出转换为字节字符串

    在 Python 3 中，tzname() API 发生了变化。它曾经返回字节字符串，但在 Python 3 中被更改为返回 Unicode 字符串。
    """
    def convert_to_string(name):
        # 如果是None直接返回
        if name is None:
            return None
            
        # 如果是bytes类型直接返回
        if isinstance(name, bytes):
            return name
            
        # 如果是unicode类型,转换为bytes
        if isinstance(name, str):
            return name.encode('ascii')
            
        # 其他类型抛出异常
        raise TypeError('tzname must return None or a string')
        
    def wrapper(*args, **kwargs):
        result = namefunc(*args, **kwargs)
        
        # 如果返回的是元组(处理多个时区名称的情况)
        if isinstance(result, tuple):
            return tuple(convert_to_string(n) for n in result)
            
        return convert_to_string(result)
        
    return wrapper