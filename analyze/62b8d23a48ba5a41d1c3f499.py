def popitem(self):
    """
    Elimina y devuelve el par (clave, valor) menos recientemente utilizado.
    """
    if not self.data:
        raise KeyError("popitem(): dictionary is empty")
    
    # Find the least recently used item
    lru_key = next(iter(self.data))
    lru_value = self.data[lru_key]
    
    # Remove the item from the dictionary
    del self.data[lru_key]
    
    return lru_key, lru_value