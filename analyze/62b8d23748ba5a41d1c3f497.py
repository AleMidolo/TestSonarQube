def popitem(self):
    """
    移除并返回最少使用的键值对。
    """
    if not self:
        raise KeyError("popitem(): dictionary is empty")
    
    # Find the least recently used item
    lru_key = next(iter(self))
    for key in self:
        if self[key] < self[lru_key]:
            lru_key = key
    
    # Remove and return the least recently used item
    value = self.pop(lru_key)
    return (lru_key, value)