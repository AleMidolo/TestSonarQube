import random

def popitem(self):
    """
    在类中通过 `__choice` 方法查找、移除并返回一个随机的键值对。
    移除并返回一个随机的键值对。
    """
    if not self:
        raise KeyError("popitem(): dictionary is empty")
    
    key = random.choice(list(self.keys()))
    value = self.pop(key)
    return (key, value)