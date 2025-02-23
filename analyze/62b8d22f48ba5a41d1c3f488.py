def popitem(self):
    """  
    पहले डाली गई `(key, value)` जोड़ी को हटाएं और लौटाएं।
    """
    if not self.data:
        raise KeyError("popitem(): dictionary is empty")
    key = next(iter(self.data))
    value = self.data[key]
    del self.data[key]
    return key, value