def get(self, key, default=None):
    try:
        return self[key]
    except KeyError:
        return default