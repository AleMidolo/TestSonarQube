def popitem(self):
    """
    Rimuove e restituisce la coppia `(chiave, valore)` meno frequentemente utilizzata.
    """
    if not self.cache:  # if cache is empty
        raise KeyError("Cache is empty")
        
    # Find item with minimum frequency
    min_freq = min(self.freq_map.values())
    
    # Find first key with minimum frequency
    min_key = None
    for key in self.freq_map:
        if self.freq_map[key] == min_freq:
            min_key = key
            break
            
    # Get value before removing
    min_value = self.cache[min_key]
    
    # Remove item from cache and frequency map
    del self.cache[min_key]
    del self.freq_map[min_key]
    
    return (min_key, min_value)