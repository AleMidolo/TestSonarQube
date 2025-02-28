def popitem(self):
    """
    删除与第一个插入的键对应的值，并以元组 `(key, value)` 的格式返回。
    删除并返回第一个插入的 `(key, value)` 键值对。
    """
    if not self:
        raise KeyError("popitem(): dictionary is empty")
    key = next(iter(self))
    value = self.pop(key)
    return (key, value)