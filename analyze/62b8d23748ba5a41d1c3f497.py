def popitem(self):
    """
    Remove and return the `(key, value)` pair least frequently used.
    """
    if not self.freq_map:
        raise KeyError("popitem(): dictionary is empty")
    
    # Find the least frequently used key
    least_freq = min(self.freq_map.values())
    least_freq_keys = [key for key, freq in self.freq_map.items() if freq == least_freq]
    
    # If there are multiple keys with the same frequency, we can choose any
    least_freq_key = least_freq_keys[0]
    
    # Remove the key from the frequency map and the main dictionary
    value = self.data.pop(least_freq_key)
    del self.freq_map[least_freq_key]
    
    return least_freq_key, value