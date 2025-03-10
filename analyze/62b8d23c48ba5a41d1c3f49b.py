def popitem(self):
    """
    移除并返回最近使用的键值对。
    """
    if not self:
        raise KeyError("popitem(): dictionary is empty")
    key = next(reversed(self))
    value = self[key]
    del self[key]
    return (key, value)