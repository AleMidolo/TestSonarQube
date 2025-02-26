def popitem(self):
    """
    सबसे कम बार उपयोग किए गए `(key, value)` जोड़े को हटाएं और वापस करें।
    """
    if not self.data:
        raise KeyError("popitem(): dictionary is empty")
    
    # Find the least frequently used item
    least_used_key = min(self.usage_count, key=self.usage_count.get)
    value = self.data.pop(least_used_key)
    del self.usage_count[least_used_key]
    
    return least_used_key, value