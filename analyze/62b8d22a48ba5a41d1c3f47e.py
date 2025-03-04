def setdefault(self, key, default=None):
    """
    `D.setdefault(k[,d]) -> D.get(k,d)`, imposta anche `D[k]=d` se `k` non è presente in `D`.
    """
    if key not in self:
        self[key] = default
    return self[key]