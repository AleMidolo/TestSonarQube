def popitem(self):
    """
    Remove and return the `(key, value)` pair least frequently used.
    """
    if not self:
        raise KeyError("Dictionary is empty")
        
    # Find the entry with minimum frequency
    min_freq = min(self.freq.values())
    
    # Get the first key with minimum frequency
    lfu_key = next(key for key, freq in self.freq.items() if freq == min_freq)
    
    # Get the value for this key
    lfu_value = self[lfu_key]
    
    # Remove the key-value pair
    del self[lfu_key]
    del self.freq[lfu_key]
    
    return (lfu_key, lfu_value)