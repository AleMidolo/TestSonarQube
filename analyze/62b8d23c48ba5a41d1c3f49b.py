def popitem(self):
    """
    सबसे हाल ही में उपयोग किए गए `(कुंजी, मान)` जोड़े को हटाएं और वापस करें।
    """
    if not self:
        raise KeyError('Dictionary is empty')
        
    # Get the most recently used key from the internal ordering
    key = next(reversed(self))
    value = self[key]
    
    # Remove the key-value pair
    del self[key]
    
    return (key, value)