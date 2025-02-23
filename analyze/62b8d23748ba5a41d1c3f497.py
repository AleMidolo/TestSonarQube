def popitem(self):
    """
    移除并返回最少使用的键值对。
    """
    if not self.data:
        raise KeyError("popitem(): dictionary is empty")
    
    # Assuming self.data is a dictionary-like structure with usage tracking
    least_used_key = min(self.usage, key=self.usage.get)
    value = self.data.pop(least_used_key)
    del self.usage[least_used_key]
    
    return least_used_key, value