def setdefault(self, key, default=None):
    try:
        return self[key]
    except KeyError:
        self[key] = default
        return default