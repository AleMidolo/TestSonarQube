def get(self, key, default=None):
    """
    `D.get(k[, d]) -> D[k]` se `k` è presente in `D`, altrimenti `d`. Il valore predefinito di `d` è `None`.
    """
    if key in self:
        return self[key]
    else:
        return default