def popitem(self):
    """
    移除并返回最少使用的键值对。
    """
    if not self:
        raise KeyError("popitem(): dictionary is empty")
    
    # Find the least recently used key
    lru_key = next(iter(self))
    
    # Remove the key-value pair
    value = self.pop(lru_key)
    
    return (lru_key, value)