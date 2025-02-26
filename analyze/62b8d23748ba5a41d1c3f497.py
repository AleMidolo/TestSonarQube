def popitem(self):
    """
    सबसे कम बार उपयोग किए गए `(key, value)` जोड़े को हटाएं और वापस करें।
    """
    if not self.data:
        raise KeyError("popitem(): dictionary is empty")
    
    # Find the key with the minimum usage count
    min_key = min(self.usage_count, key=self.usage_count.get)
    
    # Remove the item from both data and usage_count
    value = self.data.pop(min_key)
    del self.usage_count[min_key]
    
    return (min_key, value)