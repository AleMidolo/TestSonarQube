def popitem(self):
    """
    पहले डाली गई `(key, value)` जोड़ी को हटाएं और लौटाएं।
    """
    if not self:
        raise KeyError("dictionary is empty")
    key = next(iter(self))
    value = self.pop(key)
    return (key, value)