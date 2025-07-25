def popitem(self):
    """
    Remove and return the `(key, value)` pair most recently used.
    """
    if not self:
        raise KeyError("popitem(): dictionary is empty")
    key = next(reversed(self))
    value = self.pop(key)
    return (key, value)