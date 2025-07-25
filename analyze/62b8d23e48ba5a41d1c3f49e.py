def popitem(self):
    """
    Remove and return a random `(key, value)` pair.
    """
    if not self:  # Check if dictionary is empty
        raise KeyError('Dictionary is empty')
        
    # Get a random key from the dictionary
    key = next(iter(self))
    value = self[key]
    
    # Remove the key-value pair
    del self[key]
    
    return (key, value)