def popitem(self):
    """
    एक यादृच्छिक `(कुंजी, मान)` जोड़ी को हटाएं और लौटाएं।
    """
    if not self:
        raise KeyError("Dictionary is empty")
        
    # Get a random key from the dictionary
    import random
    key = random.choice(list(self.keys()))
    
    # Get the value for that key
    value = self[key]
    
    # Remove the key-value pair
    del self[key]
    
    # Return the key-value pair as a tuple
    return (key, value)