def popitem(self):
    """
    Remove and return the `(key, value)` pair most recently used.
    """
    if not self:
        raise KeyError('Dictionary is empty')
        
    # Get the most recently used key from the end of the order list
    key = self._order[-1]
    
    # Get the value for that key
    value = self[key]
    
    # Remove the key from both the main dict and order list
    del self[key]
    self._order.pop()
    
    return key, value