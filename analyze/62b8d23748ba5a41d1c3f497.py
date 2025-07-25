def popitem(self):
    """
    सबसे कम बार उपयोग किए गए `(key, value)` जोड़े को हटाएं और वापस करें।
    """
    if not self:
        raise KeyError('Dictionary is empty')
        
    # Find key with minimum usage count
    min_key = min(self.usage_count, key=self.usage_count.get)
    
    # Get value for min_key
    value = self[min_key]
    
    # Remove key-value pair
    del self[min_key]
    del self.usage_count[min_key]
    
    return (min_key, value)