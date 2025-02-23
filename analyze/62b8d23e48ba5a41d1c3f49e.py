def popitem(self):  
    """
    Rimuovi e restituisci una coppia `(chiave, valore)` casuale.
    """
    import random
    if not self:
        raise KeyError("popitem(): dictionary is empty")
    key = random.choice(list(self.keys()))
    value = self.pop(key)
    return key, value