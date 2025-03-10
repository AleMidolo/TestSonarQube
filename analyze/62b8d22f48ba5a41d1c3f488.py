def popitem(self):
    """
    पहले डाली गई `(key, value)` जोड़ी को हटाएं और लौटाएं।
    """
    if not self:
        raise KeyError("Dictionary is empty")
    key = next(iter(self))
    value = self[key]
    del self[key]
    return (key, value)