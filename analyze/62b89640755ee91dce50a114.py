def tzname_in_python2(namefunc):
    """
    Cambiar la salida de unicode a cadenas de bytes en Python 2

    La API tzname() cambió en Python 3. Solía devolver bytes, pero fue modificada
    para devolver cadenas unicode.
    """
    def adjust_encoding(*args, **kwargs):
        name = namefunc(*args, **kwargs)
        if name is not None:
            name = name.encode('UTF-8')
        return name
        
    return adjust_encoding