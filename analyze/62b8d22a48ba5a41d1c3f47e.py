def setdefault(self, key, default=None):
    """
    D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D
    """
    try:
        return self[key]
    except KeyError:
        self[key] = default
        return default