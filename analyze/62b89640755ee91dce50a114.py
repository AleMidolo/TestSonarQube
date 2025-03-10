def tzname_in_python2(namefunc):
    """
    Modifica l'output unicode in stringhe di byte in Python 2

    L'API tzname() è cambiata in Python 3. In precedenza restituiva stringhe di byte, ma è stata modificata per restituire stringhe unicode.
    """
    def wrapper(*args, **kwargs):
        result = namefunc(*args, **kwargs)
        if isinstance(result, unicode):
            return result.encode('utf-8')
        elif isinstance(result, tuple):
            return tuple(item.encode('utf-8') if isinstance(item, unicode) else item for item in result)
        return result
    return wrapper