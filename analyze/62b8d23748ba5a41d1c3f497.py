def popitem(self):
    """
    移除并返回最少使用的键值对。
    """
    if not self.cache:
        raise KeyError("popitem(): cache is empty")
    
    # Find the least recently used item
    least_used_key = min(self.cache, key=self.cache.get)
    least_used_value = self.cache.pop(least_used_key)
    
    return least_used_key, least_used_value