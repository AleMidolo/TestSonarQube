def get(self, key, default=None):
    """
    D.get(k[, d]) -> D[k] si k está en D, de lo contrario d. d tiene como valor predeterminado 'None'.
    """
    if key in self:
        return self[key]
    else:
        return default