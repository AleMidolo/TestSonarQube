def tzname_in_python2(namefunc):
    def wrapper(*args, **kwargs):
        return namefunc(*args, **kwargs).encode('utf-8')
    return wrapper