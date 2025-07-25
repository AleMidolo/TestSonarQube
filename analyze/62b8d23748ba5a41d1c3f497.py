def popitem(self):
    """
    Rimuove e restituisce la coppia `(chiave, valore)` meno frequentemente utilizzata.
    """
    if not self.cache:  # if cache is empty
        raise KeyError("Cache is empty")
        
    # Find item with minimum frequency
    min_freq = min(self.freq_map.keys())
    
    # Get the least recently used item from that frequency
    lru_list = self.freq_map[min_freq]
    key = lru_list.pop()
    
    # If frequency list becomes empty, remove it
    if not lru_list:
        del self.freq_map[min_freq]
        
    # Get value and remove from cache
    value = self.cache[key]
    del self.cache[key]
    del self.key_freq[key]
    
    return (key, value)