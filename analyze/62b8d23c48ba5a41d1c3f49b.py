def popitem(self):
    """
    Remove and return the `(key, value)` pair most recently used.
    """
    if not self:
        raise KeyError('Dictionary is empty')
        
    # Get the most recently used key from the end of the order list
    key = self._order[-1]
    value = self[key]
    
    # Remove the key-value pair
    del self[key]
    
    return key, value