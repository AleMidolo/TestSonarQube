def pop(self, key, default=__marker):
    """
    D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
    If key is not found, d is returned if given, otherwise KeyError is raised.
    """
    try:
        value = self[key]
        del self[key]
        return value
    except KeyError:
        if default is __marker:
            raise
        return default