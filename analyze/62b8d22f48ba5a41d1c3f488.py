def popitem(self):
    """  
    पहले डाली गई `(key, value)` जोड़ी को हटाएं और लौटाएं।
    """
    if not self.items:
        raise KeyError("popitem(): dictionary is empty")
    key = next(iter(self.items))
    value = self.items[key]
    del self.items[key]
    return key, value