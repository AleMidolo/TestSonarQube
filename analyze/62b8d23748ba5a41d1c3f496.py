from functools import wraps
from collections import defaultdict, OrderedDict

def lfu_cache(maxsize=128, typed=False):
    def decorator(func):
        cache = {}
        frequency = defaultdict(int)
        freq_map = defaultdict(OrderedDict)
        min_freq = 0

        @wraps(func)
        def wrapper(*args, **kwargs):
            if typed:
                key = (args, tuple(sorted(kwargs.items())))
            else:
                key = args + tuple(sorted(kwargs.items()))

            if key in cache:
                # Increment frequency and update frequency map
                freq = frequency[key]
                frequency[key] += 1
                del freq_map[freq][key]
                if not freq_map[freq]:
                    del freq_map[freq]
                    if freq == min_freq:
                        min_freq += 1
                freq_map[freq + 1][key] = None
                return cache[key]

            # If cache is full, evict the least frequently used item
            if len(cache) >= maxsize:
                evict_key, _ = freq_map[min_freq].popitem(last=False)
                if not freq_map[min_freq]:
                    del freq_map[min_freq]
                del cache[evict_key]
                del frequency[evict_key]

            # Add new item to cache
            result = func(*args, **kwargs)
            cache[key] = result
            frequency[key] = 1
            freq_map[1][key] = None
            min_freq = 1
            return result

        return wrapper
    return decorator