def popitem(self):
    """
    Remove and return the `(key, value)` pair least frequently used.
    """
    if not self:
        raise KeyError("popitem(): dictionary is empty")
    
    # Find the key with the minimum frequency
    min_key = min(self.keys(), key=lambda k: self[k])
    
    # Remove and return the (key, value) pair
    value = self.pop(min_key)
    return (min_key, value)