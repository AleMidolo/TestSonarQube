def popitem(self):
    """
    Rimuove e restituisce la coppia `(chiave, valore)` meno frequentemente utilizzata.
    """
    if not self.data:
        raise KeyError("popitem(): dictionary is empty")
    
    # Trova la chiave con il valore di accesso minimo
    min_key = min(self.access_count, key=self.access_count.get)
    
    # Rimuove la chiave dalla struttura dati
    value = self.data.pop(min_key)
    del self.access_count[min_key]
    
    return (min_key, value)