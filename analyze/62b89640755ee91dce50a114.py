def tzname_in_python2(namefunc):
    """
    Cambiar la salida de unicode a cadenas de bytes en Python 2

    La API tzname() cambió en Python 3. Solía devolver bytes, pero fue modificada
    para devolver cadenas unicode.
    """
    def wrapper(*args, **kwargs):
        return namefunc(*args, **kwargs).encode('utf-8')
    return wrapper