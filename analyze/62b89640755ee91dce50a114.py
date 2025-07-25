def tzname_in_python2(namefunc):
    """
    在 Python 2 中将 Unicode 输出转换为字节字符串

    在 Python 3 中，tzname() API 发生了变化。它曾经返回字节字符串，但在 Python 3 中被更改为返回 Unicode 字符串。
    """
    def convert_to_string(*args, **kwargs):
        result = namefunc(*args, **kwargs)
        if result is None:
            return None
        elif isinstance(result, str):
            return result
        elif isinstance(result, unicode):
            return result.encode('UTF-8')
        else:
            raise TypeError('tzname must return None or a string')
    return convert_to_string