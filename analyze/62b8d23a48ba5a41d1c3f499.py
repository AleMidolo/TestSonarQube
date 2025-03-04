def popitem(self):
    """
    Rimuove e restituisce la coppia `(chiave, valore)` meno recentemente utilizzata.
    """
    if not self.data:
        raise KeyError("popitem(): dictionary is empty")
    
    # Trova la chiave meno recentemente utilizzata
    lru_key = next(iter(self.data))
    lru_value = self.data[lru_key]
    
    # Rimuove la coppia dal dizionario
    del self.data[lru_key]
    
    return lru_key, lru_value