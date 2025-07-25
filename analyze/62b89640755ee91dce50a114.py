def tzname_in_python2(namefunc):
    """
    Modifica l'output unicode in stringhe di byte in Python 2

    L'API tzname() è cambiata in Python 3. In precedenza restituiva stringhe di byte, ma è stata modificata per restituire stringhe unicode.
    """
    def adjust_encoding(*args, **kwargs):
        name = namefunc(*args, **kwargs)
        if name is not None and isinstance(name, unicode):
            name = name.encode()
        return name
    return adjust_encoding