import random

def popitem(self):
    if not self:
        raise KeyError("popitem(): dictionary is empty")
    key = random.choice(list(self.keys()))
    value = self.pop(key)
    return key, value