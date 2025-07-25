def get(self, key, default=None):
    """
    D.get(k[, d]) -> D[k] si k está en D, de lo contrario d. d tiene como valor predeterminado 'None'.
    """
    try:
        return self[key]
    except KeyError:
        return default