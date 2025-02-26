def popitem(self):
    """
    Remove and return the `(key, value)` pair least recently used.
    """
    if not self.cache:
        raise KeyError("popitem(): cache is empty")
    
    # Remove the first item from the ordered dictionary
    key, value = self.cache.popitem(last=False)
    return key, value