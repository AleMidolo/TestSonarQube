import random

class CustomDict:
    def __init__(self):
        self.data = {}

    def popitem(self):
        """
        Remove and return a random `(key, value)` pair.
        """
        if not self.data:
            raise KeyError("popitem(): dictionary is empty")
        key = random.choice(list(self.data.keys()))
        value = self.data.pop(key)
        return key, value