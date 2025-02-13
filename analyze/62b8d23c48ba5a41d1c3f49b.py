def popitem(self):  
    """
    Rimuove e restituisce la coppia `(chiave, valore)` utilizzata più di recente.
    """
    if not self.data:
        raise KeyError("popitem(): dictionary is empty")
    key = next(reversed(self.data))
    value = self.data.pop(key)
    return key, value