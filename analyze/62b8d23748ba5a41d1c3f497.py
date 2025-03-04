def popitem(self):
    """
    Rimuove e restituisce la coppia `(chiave, valore)` meno frequentemente utilizzata.
    """
    if not self.data:
        raise KeyError("popitem(): dictionary is empty")
    
    # Trova la chiave con il valore di accesso minimo
    least_frequent_key = min(self.frequency, key=self.frequency.get)
    
    # Rimuove la chiave dalla struttura dati
    value = self.data.pop(least_frequent_key)
    del self.frequency[least_frequent_key]
    
    return least_frequent_key, value