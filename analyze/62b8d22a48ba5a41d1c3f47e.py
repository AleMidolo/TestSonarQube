def setdefault(self, key, default=None):
    """
    D.setdefault(k[, d]) -> D.get(k, d)
    साथ ही, यदि `k` (कुंजी) `D` (डिक्शनरी) में मौजूद नहीं है, तो `D[k] = d` सेट कर दिया जाता है।
    """
    if key in self:
        return self[key]
    else:
        self[key] = default
        return default