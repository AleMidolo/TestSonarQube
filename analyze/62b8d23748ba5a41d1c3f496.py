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
                # Increment frequency
                freq = frequency[key]
                frequency[key] += 1
                del frequency_list[freq][key]
                frequency_list[freq + 1][key] = None
                if freq == min_freq and not frequency_list[freq]:
                    min_freq += 1
                return cache[key]

            result = func(*args, **kwargs)

            if len(cache) >= maxsize:
                # Evict the least frequently used item
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