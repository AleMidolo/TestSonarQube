def popitem(self):
    """
    Remove and return the `(key, value)` pair first inserted.
    """
    if not self:
        raise KeyError("popitem(): dictionary is empty")
    
    first_key = next(iter(self))
    value = self[first_key]
    del self[first_key]
    return first_key, value