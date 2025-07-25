def popitem(self):
    """
    सबसे कम बार उपयोग किए गए `(key, value)` जोड़े को हटाएं और वापस करें।
    """
    if not self:
        raise KeyError("popitem(): dictionary is empty")
    
    # Find the key with the least frequency
    min_key = min(self, key=lambda k: self[k])
    
    # Remove and return the (key, value) pair
    value = self.pop(min_key)
    return (min_key, value)