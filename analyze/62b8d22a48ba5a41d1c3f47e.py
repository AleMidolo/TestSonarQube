def setdefault(self, key, default=None):
    """
    `D.setdefault(k[, d]) -> D.get(k, d)`, también establece `D[k] = d` si `k` no está en `D`.
    """
    if key not in self:
        self[key] = default
    return self.get(key, default)