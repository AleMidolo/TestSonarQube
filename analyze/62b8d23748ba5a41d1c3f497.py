def popitem(self):
    """
    Rimuove e restituisce la coppia `(chiave, valore)` meno frequentemente utilizzata.
    """
    if not self.data:
        raise KeyError("popitem(): dictionary is empty")
    
    # Trova la chiave meno frequentemente utilizzata
    least_used_key = min(self.usage_count, key=self.usage_count.get)
    
    # Rimuovi la chiave dal dizionario e dalla conta
    value = self.data.pop(least_used_key)
    del self.usage_count[least_used_key]
    
    return (least_used_key, value)