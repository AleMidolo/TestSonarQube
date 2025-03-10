def tzname_in_python2(namefunc):
    """
    Change unicode output into bytestrings in Python 2

    tzname() API changed in Python 3. It used to return bytes, but was changed
    to unicode strings
    """
    def wrapper(*args, **kwargs):
        result = namefunc(*args, **kwargs)
        if isinstance(result, tuple):
            return tuple(s.encode('utf-8') if isinstance(s, unicode) else s for s in result)
        elif isinstance(result, unicode):
            return result.encode('utf-8')
        return result
    return wrapper