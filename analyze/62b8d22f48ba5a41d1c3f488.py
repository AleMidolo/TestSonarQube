def popitem(self):
    if not self:
        raise KeyError("popitem(): dictionary is empty")
    first_key = next(iter(self))
    value = self[first_key]
    del self[first_key]
    return (first_key, value)