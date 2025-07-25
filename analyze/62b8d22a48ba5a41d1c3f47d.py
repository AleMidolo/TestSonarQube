def pop(self, key, default=__marker):
    if key in self:
        value = self[key]
        del self[key]
        return value
    elif default is not __marker:
        return default
    else:
        raise KeyError(f"KeyError: '{key}'")