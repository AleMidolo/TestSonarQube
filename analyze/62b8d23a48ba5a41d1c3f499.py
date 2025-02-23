def popitem(self):
    """
    Rimuove e restituisce la coppia `(chiave, valore)` meno recentemente utilizzata.
    """
    if not self.data:
        raise KeyError("popitem(): dictionary is empty")
    
    # Trova la chiave meno recentemente utilizzata
    lru_key = next(iter(self.data))
    
    # Rimuove la chiave dal dizionario e restituisce la coppia
    value = self.data.pop(lru_key)
    return lru_key, value