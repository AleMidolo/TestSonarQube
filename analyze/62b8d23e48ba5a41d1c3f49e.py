def popitem(self):
    """
    Remove and return a random `(key, value)` pair.
    """
    import random
    if not self:
        raise KeyError("popitem(): dictionary is empty")
    key = random.choice(list(self.keys()))
    value = self.pop(key)
    return key, value