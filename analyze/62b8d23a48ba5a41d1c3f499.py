def popitem(self):
    """
    移除并返回最久未使用的键值对。
    """
    if not self:
        raise KeyError("popitem(): dictionary is empty")
    key = next(iter(self))
    value = self.pop(key)
    return (key, value)