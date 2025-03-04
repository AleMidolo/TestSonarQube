def popitem(self):
    """
    Rimuove e restituisce la coppia `(chiave, valore)` utilizzata più di recente.
    """
    if not self:
        raise KeyError('Dictionary is empty')
        
    # Get the most recently used key from the end of the order list
    key = self._order[-1]
    
    # Get the value for this key
    value = self[key]
    
    # Remove the key from both the main dict and order list
    del self[key]
    self._order.pop()
    
    # Return the key-value pair
    return (key, value)