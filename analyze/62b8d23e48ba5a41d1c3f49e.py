import random

class MyDict:
    def __init__(self):
        self.data = {}

    def popitem(self):
        if not self.data:
            raise KeyError("popitem(): dictionary is empty")
        key = random.choice(list(self.data.keys()))
        value = self.data.pop(key)
        return key, value