def popitem(self):
    """
    Rimuove e restituisce la coppia `(chiave, valore)` meno frequentemente utilizzata.
    """
    if not self:
        raise KeyError("popitem(): dictionary is empty")
    
    # Trova la chiave con il valore minimo (meno frequentemente utilizzata)
    min_key = min(self, key=self.get)
    
    # Rimuovi e restituisci la coppia (chiave, valore)
    return min_key, self.pop(min_key)