def popitem(self):
    """
    移除并返回最少使用的键值对。
    """
    if not self:
        raise KeyError("popitem(): dictionary is empty")
    
    # Assuming self is a dictionary-like object with a method to track usage
    # Here we assume that the least recently used item is the first one in the dictionary
    # This is a simplified implementation and may not be accurate for all use cases
    key = next(iter(self))
    value = self.pop(key)
    return key, value