def lfu_cache(maxsize=128, typed=False):
    """
    Decorator per racchiudere una funzione con un oggetto callable di memoizzazione
    che salva fino a `maxsize` risultati basandosi su un algoritmo Least Frequently Used (LFU).
    """
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

    def decorator(func):
        cache = LFUCache(maxsize)

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if typed:
                key = (args, frozenset(kwargs.items()))
            else:
                key = args
            result = cache.get(key)
            if result == -1:
                result = func(*args, **kwargs)
                cache.put(key, result)
            return result

        return wrapper

    return decorator