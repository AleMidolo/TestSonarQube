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

        def _update(self, key):
            freq = self.cache[key][1]
            self.freq[freq].pop(key)
            if not self.freq[freq]:
                if self.min_freq == freq:
                    self.min_freq += 1
                del self.freq[freq]
            self.cache[key][1] += 1
            self.freq[self.cache[key][1]][key] = self.cache[key]

        def get(self, key):
            if key not in self.cache:
                return None
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

    def decorator(func):
        cache = LFUCache(maxsize)

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if typed:
                key = (args, frozenset(kwargs.items()))
            else:
                key = args
            result = cache.get(key)
            if result is None:
                result = func(*args, **kwargs)
                cache.put(key, result)
            return result

        return wrapper

    return decorator