def pop(self, key, default=__marker):
    """
    `D.pop(k[, d]) -> v`：移除指定的键并返回对应的值。  
    如果未找到指定的键，则返回 `d`（如果提供了 `d`）；否则会引发 `KeyError` 异常。
    """
    if key in self:
        value = self[key]
        del self[key]
        return value
    elif default is not __marker:
        return default
    else:
        raise KeyError(key)