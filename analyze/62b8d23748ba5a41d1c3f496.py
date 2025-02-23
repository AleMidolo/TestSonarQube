from collections import defaultdict
from functools import wraps

class LFUCache:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.cache = {}
        self.freq = defaultdict(int)
        self.min_freq = 0
        self.freq_map = defaultdict(set)

    def get(self, key):
        if key not in self.cache:
            return None
        self.freq[key] += 1
        self.freq_map[self.freq[key]].add(key)
        self.freq_map[self.freq[key] - 1].remove(key)
        if not self.freq_map[self.min_freq]:
            self.min_freq += 1
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            self.cache[key] = value
            self.get(key)  # Update frequency
            return
        if len(self.cache) >= self.maxsize:
            lfu_key = self.freq_map[self.min_freq].pop()
            del self.cache[lfu_key]
            self.freq.pop(lfu_key)
        self.cache[key] = value
        self.freq[key] = 1
        self.min_freq = 1
        self.freq_map[1].add(key)

def lfu_cache(maxsize=128, typed=False):
    def decorator(func):
        cache = LFUCache(maxsize)

        @wraps(func)
        def wrapper(*args, **kwargs):
            if typed:
                key = (args, frozenset(kwargs.items()))
            else:
                key = (tuple(args), frozenset(kwargs.items()))
            result = cache.get(key)
            if result is None:
                result = func(*args, **kwargs)
                cache.put(key, result)
            return result

        return wrapper

    return decorator