from collections import defaultdict, OrderedDict
import functools

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
        if self.maxsize <= 0:
            return
        if key in self.cache:
            self.cache[key] = (value, self.cache[key][1])
            self.get(key)
            return
        if len(self.cache) >= self.maxsize:
            evict_key, _ = self.freq[self.min_freq].popitem(last=False)
            del self.cache[evict_key]
        self.cache[key] = (value, 1)
        self.freq[1][key] = value
        self.min_freq = 1

def lfu_cache(maxsize=128, typed=False):
    def decorator(func):
        cache = LFUCache(maxsize)

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if typed:
                key = (tuple(args), frozenset(kwargs.items()))
            else:
                key = (tuple(map(str, args)), frozenset((str(k), str(v)) for k, v in kwargs.items()))
            if key in cache.cache:
                return cache.get(key)
            result = func(*args, **kwargs)
            cache.put(key, result)
            return result

        return wrapper

    return decorator