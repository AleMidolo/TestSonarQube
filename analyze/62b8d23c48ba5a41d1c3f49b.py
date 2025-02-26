def popitem(self):
    """
    移除并返回最近使用的键值对。
    """
    if not self.data:
        raise KeyError("popitem(): dictionary is empty")
    key, value = self.data.popitem()
    self.order.remove(key)
    return key, value