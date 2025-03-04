def popitem(self):
    """
    पहले डाली गई `(key, value)` जोड़ी को हटाएं और लौटाएं।
    """
    if not self:  # If dictionary is empty
        raise KeyError("Dictionary is empty")
        
    # Get the first key-value pair (oldest inserted item)
    first_key = next(iter(self))
    value = self[first_key]
    
    # Remove the item from dictionary
    del self[first_key]
    
    # Return the key-value pair as a tuple
    return (first_key, value)