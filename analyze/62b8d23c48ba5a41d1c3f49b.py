def popitem(self):
    """
    移除并返回最近使用的键值对。
    """
    if not self.data:
        raise KeyError("popitem(): dictionary is empty")
    key = self.order.pop()  # Assuming self.order keeps track of the order of keys
    value = self.data.pop(key)
    return key, value