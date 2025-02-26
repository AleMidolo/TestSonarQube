from collections import defaultdict, OrderedDict
import functools

class LFUCache:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.cache = {}
        self.freq = defaultdict(OrderedDict)
        self.min_freq = 0

    def _update(self, key):
        freq = self.cache[key][1]
        self.freq[freq].pop(key)
        if not self.freq[freq]:
            del self.freq[freq]
            if self.min_freq == freq:
                self.min_freq += 1
        self.cache[key][1] += 1
        self.freq[freq + 1][key] = self.cache[key]
    
    def get(self, key):
        if key not in self.cache:
            return -1
        self._update(key)
        return self.cache[key][0]

    def put(self, key, value):
        if key in self.cache:
            self.cache[key] = (value, self.cache[key][1])
            self._update(key)
            return
        if len(self.cache) >= self.maxsize:
            lfu_key, _ = self.freq[self.min_freq].popitem(last=False)
            del self.cache[lfu_key]
        self.cache[key] = (value, 1)
        self.freq[1][key] = self.cache[key]
        self.min_freq = 1

def lfu_cache(maxsize=128, typed=False):
    """
    一个用于将函数包装为一个带有记忆功能的可调用对象的装饰器，
    该对象基于最少使用频率（LFU，Least Frequently Used）算法，
    保存最多 `maxsize` 个结果。
    """
    def decorator(func):
        cache = LFUCache(maxsize)

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if typed:
                key = (tuple(args), frozenset(kwargs.items()))
            else:
                key = tuple(args) + tuple(sorted(kwargs.items()))
            result = cache.get(key)
            if result == -1:
                result = func(*args, **kwargs)
                cache.put(key, result)
            return result

        return wrapper

    return decorator