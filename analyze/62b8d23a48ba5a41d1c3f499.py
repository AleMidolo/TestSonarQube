def popitem(self):
    """
    移除并返回最久未使用的键值对。
    """
    if not self.data:
        raise KeyError("popitem(): dictionary is empty")
    
    oldest_key = next(iter(self.data))
    value = self.data.pop(oldest_key)
    return oldest_key, value