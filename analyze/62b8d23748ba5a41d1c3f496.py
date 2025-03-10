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
            if typed:
                key = (args, tuple(sorted(kwargs.items())))
            else:
                key = args + tuple(sorted(kwargs.items()))

            if key in cache:
                # Increment frequency and move to the next frequency list
                freq = frequency[key]
                frequency[key] += 1
                del frequency_list[freq][key]
                if not frequency_list[freq]:
                    del frequency_list[freq]
                    if freq == min_freq:
                        min_freq += 1
                frequency_list[freq + 1][key] = None
                return cache[key]

            # If cache is full, evict the least frequently used item
            if len(cache) >= maxsize:
                evict_key, _ = frequency_list[min_freq].popitem(last=False)
                del cache[evict_key]
                del frequency[evict_key]

            # Add new item to cache
            result = func(*args, **kwargs)
            cache[key] = result
            frequency[key] = 1
            frequency_list[1][key] = None
            min_freq = 1
            return result

        return wrapper
    return decorator