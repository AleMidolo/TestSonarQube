def pop(self, key, default=__marker):
    try:
        value = self[key]
        del self[key]
        return value
    except KeyError:
        if default is not __marker:
            return default
        raise