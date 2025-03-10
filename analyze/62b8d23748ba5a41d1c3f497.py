def popitem(self):
    """
    सबसे कम बार उपयोग किए गए `(key, value)` जोड़े को हटाएं और वापस करें।
    """
    if not self:
        raise KeyError("popitem(): dictionary is empty")
    
    # Find the key with the least frequency
    least_frequent_key = min(self.keys(), key=lambda k: self[k])
    
    # Remove and return the (key, value) pair
    value = self.pop(least_frequent_key)
    return (least_frequent_key, value)