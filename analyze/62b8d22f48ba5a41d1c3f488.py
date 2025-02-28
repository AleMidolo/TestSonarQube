def popitem(self):
    """
    Remove and return the `(key, value)` pair first inserted.
    """
    if not self:
        raise KeyError("dictionary is empty")
    key = next(iter(self))
    value = self.pop(key)
    return (key, value)