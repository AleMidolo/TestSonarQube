def popitem(self):
    """
    Rimuove e restituisce la coppia `(chiave, valore)` meno recentemente utilizzata.
    """
    if not self.data:
        raise KeyError("popitem(): dictionary is empty")
    
    # Trova la chiave meno recentemente utilizzata
    least_recently_used_key = next(iter(self.data))
    
    # Rimuove la coppia chiave-valore
    value = self.data.pop(least_recently_used_key)
    
    return least_recently_used_key, value