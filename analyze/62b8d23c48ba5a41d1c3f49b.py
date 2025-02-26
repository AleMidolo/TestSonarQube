def popitem(self):
    """
    Remove and return the `(key, value)` pair most recently used.
    """
    if not self.data:
        raise KeyError("popitem(): dictionary is empty")
    key = next(reversed(self.data))
    value = self.data.pop(key)
    return key, value