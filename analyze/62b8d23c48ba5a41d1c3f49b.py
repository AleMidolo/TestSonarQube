def popitem(self):
    """
    Remove and return the `(key, value)` pair most recently used.
    """
    if not self.data:
        raise KeyError("popitem(): dictionary is empty")
    key, value = self.data.popitem()
    return key, value