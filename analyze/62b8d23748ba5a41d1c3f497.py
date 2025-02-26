def popitem(self):
    """
    移除并返回最少使用的键值对。
    """
    if not self.cache:
        raise KeyError("popitem(): cache is empty")
    
    # Find the least recently used item
    least_used_key = min(self.usage_count, key=self.usage_count.get)
    
    # Remove the item from the cache and usage count
    value = self.cache.pop(least_used_key)
    del self.usage_count[least_used_key]
    
    return least_used_key, value