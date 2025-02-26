def tzname_in_python2(namefunc):
    """
    在 Python 2 中将 Unicode 输出转换为字节字符串

    在 Python 3 中，tzname() API 发生了变化。它曾经返回字节字符串，但在 Python 3 中被更改为返回 Unicode 字符串。
    """
    def wrapper(*args, **kwargs):
        result = namefunc(*args, **kwargs)
        if isinstance(result, str):
            return result  # Already a byte string in Python 2
        return result.encode('utf-8')  # Convert Unicode to byte string
    return wrapper