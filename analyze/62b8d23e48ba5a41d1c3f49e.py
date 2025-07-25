def popitem(self):
    """
    Rimuovi e restituisci una coppia `(chiave, valore)` casuale.
    """
    if not self:  # se il dizionario è vuoto
        raise KeyError('Dictionary is empty')
        
    # scegli una chiave casuale
    import random
    key = random.choice(list(self.keys()))
    
    # ottieni il valore associato
    value = self[key]
    
    # rimuovi la coppia chiave-valore
    del self[key]
    
    # restituisci la coppia come tupla
    return (key, value)