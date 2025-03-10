from functools import wraps
from collections import defaultdict, OrderedDict

def lfu_cache(maxsize=128, typed=False):
    def decorator(func):
        cache = {}
        frequency = defaultdict(OrderedDict)
        min_freq = 0

        @wraps(func)
        def wrapper(*args, **kwargs):
            if typed:
                key = (args, tuple(sorted(kwargs.items())))
            else:
                key = args + tuple(sorted(kwargs.items()))

            if key in cache:
                freq = cache[key][1]
                frequency[freq].pop(key)
                if not frequency[freq]:
                    if freq == min_freq:
                        min_freq += 1
                    del frequency[freq]
                freq += 1
                frequency[freq][key] = None
                cache[key] = (cache[key][0], freq)
                return cache[key][0]

            result = func(*args, **kwargs)
            if len(cache) >= maxsize:
                evict_key, _ = frequency[min_freq].popitem(last=False)
                del cache[evict_key]
                if not frequency[min_freq]:
                    del frequency[min_freq]
                    min_freq += 1

            cache[key] = (result, 1)
            frequency[1][key] = None
            min_freq = 1
            return result

        return wrapper
    return decorator