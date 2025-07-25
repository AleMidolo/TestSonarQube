def popitem(self):
    """
    移除并返回最少使用的键值对。
    """
    if not self.cache:
        raise KeyError("popitem(): cache is empty")
    
    # Find the least recently used item
    lru_key = min(self.cache, key=self.cache.get)
    lru_value = self.cache.pop(lru_key)
    
    return lru_key, lru_value