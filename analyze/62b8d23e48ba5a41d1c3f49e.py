import random

class MyClass:
    def __init__(self):
        self.data = {}

    def __choice(self):
        if not self.data:
            return None
        return random.choice(list(self.data.items()))

    def popitem(self):
        """
        在类中通过 `__choice` 方法查找、移除并返回一个随机的键值对。
        移除并返回一个随机的键值对。
        """
        item = self.__choice()
        if item is not None:
            key, value = item
            del self.data[key]
            return key, value
        return None