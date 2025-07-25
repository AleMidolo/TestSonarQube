from functools import wraps
from collections import defaultdict, OrderedDict

def lfu_cache(maxsize=128, typed=False):
    def decorator(func):
        cache = {}
        frequency = defaultdict(int)
        frequency_list = defaultdict(OrderedDict)
        min_freq = 0

        @wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal min_freq
            key = args + tuple(sorted(kwargs.items())) if typed else args
            if key in cache:
                frequency[key] += 1
                freq = frequency[key]
                del frequency_list[freq - 1][key]
                if not frequency_list[freq - 1] and freq - 1 == min_freq:
                    min_freq += 1
                frequency_list[freq][key] = None
                return cache[key]
            result = func(*args, **kwargs)
            if len(cache) >= maxsize:
                evict_key, _ = frequency_list[min_freq].popitem(last=False)
                del cache[evict_key]
                del frequency[evict_key]
            cache[key] = result
            frequency[key] = 1
            frequency_list[1][key] = None
            min_freq = 1
            return result
        return wrapper
    return decorator