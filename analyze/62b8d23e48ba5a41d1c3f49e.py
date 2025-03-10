def popitem(self):
    if not self:
        raise KeyError("popitem(): dictionary is empty")
    key = next(iter(self))
    value = self.pop(key)
    return (key, value)