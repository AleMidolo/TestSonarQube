def popitem(self):
    """
    पहले डाली गई `(key, value)` जोड़ी को हटाएं और लौटाएं।
    """
    if not self:
        raise KeyError("Dictionary is empty")
        
    # Get first key-value pair
    first_key = next(iter(self))
    first_value = self[first_key]
    
    # Remove the pair from dictionary
    del self[first_key]
    
    # Return the removed pair as tuple
    return (first_key, first_value)