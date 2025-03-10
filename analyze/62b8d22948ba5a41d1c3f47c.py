def get(self, key, default=None):
    """
    如果类中存在指定的键（key），则返回与该键对应的值；否则，返回默认值
    如果键 `k` 存在于字典 `D` 中,则`D.get(k[, d]) -> D[k]`；否则返回默认值 `None`。
    """
    if hasattr(self, key):
        return getattr(self, key)
    return default