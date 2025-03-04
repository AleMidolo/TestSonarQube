def popitem(self):
    """
    Remove and return the `(key, value)` pair least recently used.
    """
    if not self:
        raise KeyError('Dictionary is empty')
        
    # Get the first item from the internal dict since it will be the LRU item
    key = next(iter(self))
    value = self[key]
    
    # Remove the item from the dictionary
    del self[key]
    
    return (key, value)