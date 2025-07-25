def popitem(self):
    """
    Rimuove e restituisce la coppia `(chiave, valore)` meno frequentemente utilizzata.
    """
    if not self.cache:  # if cache is empty
        raise KeyError("Cache is empty")
        
    # Find item with minimum frequency
    min_freq = min(self.freq_counter.values())
    
    # Get all items with minimum frequency
    min_freq_items = [(k,v) for k,v in self.cache.items() 
                     if self.freq_counter[k] == min_freq]
    
    # Get least recently used among min frequency items
    lru_key, lru_value = min_freq_items[0]
    
    # Remove item from cache and frequency counter
    del self.cache[lru_key]
    del self.freq_counter[lru_key]
    
    return (lru_key, lru_value)