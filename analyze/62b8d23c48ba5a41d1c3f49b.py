def popitem(self):
    """
    सबसे हाल ही में उपयोग किए गए `(कुंजी, मान)` जोड़े को हटाएं और वापस करें।
    """
    if not self:
        raise KeyError('Dictionary is empty')
        
    # Get the most recently used key
    key = next(reversed(self))
    value = self[key]
    
    # Remove the key-value pair
    del self[key]
    
    # Return the key-value pair as a tuple
    return (key, value)