def popitem(self):
    """
    Rimuove e restituisce la coppia `(chiave, valore)` meno recentemente utilizzata.
    """
    if not self._cache:  # if cache is empty
        raise KeyError("Cache is empty")
        
    # Get least recently used key (first key in ordered dict)
    lru_key = next(iter(self._cache))
    lru_value = self._cache[lru_key]
    
    # Remove the item from cache
    del self._cache[lru_key]
    
    # Return key-value pair as tuple
    return (lru_key, lru_value)