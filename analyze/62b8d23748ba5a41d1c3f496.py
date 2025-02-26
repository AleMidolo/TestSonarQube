from collections import defaultdict, OrderedDict
import functools

def lfu_cache(maxsize=128, typed=False):
    """
    一个用于将函数包装为一个带有记忆功能的可调用对象的装饰器，
    该对象基于最少使用频率（LFU，Least Frequently Used）算法，
    保存最多 `maxsize` 个结果。
    """
    class LFUCache:
        def __init__(self, maxsize):
            self.maxsize = maxsize
            self.cache = {}
            self.freq = defaultdict(OrderedDict)
            self.min_freq = 0

        def get(self, key):
            if key not in self.cache:
                return -1
            value, freq = self.cache[key]
            del self.freq[freq][key]
            if not self.freq[freq]:
                del self.freq[freq]
                if self.min_freq == freq:
                    self.min_freq += 1
            self.freq[freq + 1][key] = value
            self.cache[key] = (value, freq + 1)
            return value

        def put(self, key, value):
            if key in self.cache:
                self.cache[key] = (value, self.cache[key][1])
                self.get(key)  # Update frequency
                return
            if len(self.cache) >= self.maxsize:
                evict_key, _ = self.freq[self.min_freq].popitem(last=False)
                del self.cache[evict_key]
            self.cache[key] = (value, 1)
            self.freq[1][key] = value
            self.min_freq = 1

    cache = LFUCache(maxsize)

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if typed:
                key = (args, frozenset(kwargs.items()))
            else:
                key = (tuple(map(repr, args)), frozenset((k, repr(v)) for k, v in kwargs.items()))
            result = cache.get(key)
            if result == -1:
                result = func(*args, **kwargs)
                cache.put(key, result)
            return result
        return wrapper

    return decorator