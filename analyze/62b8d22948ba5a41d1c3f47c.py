def get(self, key, default=None):
    """
    D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None.
    """
    return self.data[key] if key in self.data else default