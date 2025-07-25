def popitem(self):
    """
    Rimuovi e restituisci una coppia `(chiave, valore)` casuale.
    """
    if not self:
        raise KeyError('Dictionary is empty')
        
    # Get a random key from the dictionary
    import random
    key = random.choice(list(self.keys()))
    
    # Get the value for that key
    value = self[key]
    
    # Remove the key-value pair
    del self[key]
    
    # Return the random key-value pair as a tuple
    return (key, value)