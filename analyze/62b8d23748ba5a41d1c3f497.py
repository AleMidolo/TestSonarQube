def popitem(self):
    """
    Rimuove e restituisce la coppia `(chiave, valore)` meno frequentemente utilizzata.
    """
    if not self:
        raise KeyError("popitem(): dictionary is empty")
    
    # Trova la chiave con il valore minimo (meno frequentemente utilizzata)
    min_key = min(self.keys(), key=lambda k: self[k])
    value = self.pop(min_key)
    return (min_key, value)