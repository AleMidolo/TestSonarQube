from functools import wraps
from collections import defaultdict, OrderedDict

def lfu_cache(maxsize=128, typed=False):
    def decorator(func):
        cache = {}
        frequency = defaultdict(int)
        freq_to_keys = defaultdict(OrderedDict)
        min_freq = 0

        @wraps(func)
        def wrapper(*args, **kwargs):
            if typed:
                key = (args, tuple(sorted(kwargs.items())))
            else:
                key = args + tuple(sorted(kwargs.items()))

            if key in cache:
                # Increment frequency
                freq = frequency[key]
                del freq_to_keys[freq][key]
                if not freq_to_keys[freq]:
                    del freq_to_keys[freq]
                    if freq == min_freq:
                        min_freq += 1
                frequency[key] += 1
                freq_to_keys[frequency[key]][key] = None
                return cache[key]

            # If cache is full, evict the least frequently used item
            if len(cache) >= maxsize:
                evict_key, _ = freq_to_keys[min_freq].popitem(last=False)
                del cache[evict_key]
                del frequency[evict_key]

            # Add new item to cache
            result = func(*args, **kwargs)
            cache[key] = result
            frequency[key] = 1
            freq_to_keys[1][key] = None
            min_freq = 1

            return result

        return wrapper

    return decorator