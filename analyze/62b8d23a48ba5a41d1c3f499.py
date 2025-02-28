def popitem(self):
    """
    Remove and return the `(key, value)` pair least recently used.
    """
    if not self:
        raise KeyError("popitem(): dictionary is empty")
    key = next(iter(self))
    value = self.pop(key)
    return (key, value)