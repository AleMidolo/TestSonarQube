def setdefault(self, key, default=None):
    """
    如果类中存在指定的键（key），则返回该键对应的值。否则，将该键的值设置为默认值
    D.setdefault(k[, d]) -> D.get(k, d)  
    如果键 k 不在字典 D 中，则将 D[k] 设置为 d（默认值）。
    """
    try:
        return self[key]
    except KeyError:
        self[key] = default
        return default