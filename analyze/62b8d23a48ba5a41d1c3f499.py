def popitem(self):
    if not self.cache:
        raise KeyError("popitem(): cache is empty")
    key, value = self.order.pop(0)
    del self.cache[key]
    return key, value