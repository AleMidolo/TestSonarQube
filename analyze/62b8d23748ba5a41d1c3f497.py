def popitem(self):
    """
    Remove and return the `(key, value)` pair least frequently used.
    """
    if not self:
        raise KeyError("Dictionary is empty")
        
    # Find the key with minimum frequency
    min_freq = min(self.freq.values())
    min_key = None
    
    # Find first key with minimum frequency
    for key in self.freq:
        if self.freq[key] == min_freq:
            min_key = key
            break
            
    # Get value for min_key
    value = self[min_key]
    
    # Remove key-value pair
    del self[min_key]
    del self.freq[min_key]
    
    return (min_key, value)