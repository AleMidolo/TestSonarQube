def setdefault(self, key, default=None):
    """
    `D.setdefault(k[, d]) -> D.get(k, d)`, también establece `D[k] = d` si `k` no está en `D`.
    """
    try:
        return self[key]
    except KeyError:
        self[key] = default
        return default