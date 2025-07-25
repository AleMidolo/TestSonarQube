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
                # Increment the frequency of the key
                freq = frequency[key]
                frequency[key] += 1
                del frequency_list[freq][key]
                if not frequency_list[freq]:
                    del frequency_list[freq]
                    if freq == min_freq:
                        min_freq += 1
                frequency_list[freq + 1][key] = None
                return cache[key]

            # If the cache is full, remove the least frequently used item
            if len(cache) >= maxsize:
                # Remove the least frequently used item
                lfu_key = next(iter(frequency_list[min_freq]))
                del cache[lfu_key]
                del frequency[lfu_key]
                del frequency_list[min_freq][lfu_key]
                if not frequency_list[min_freq]:
                    del frequency_list[min_freq]

            # Add the new item to the cache
            result = func(*args, **kwargs)
            cache[key] = result
            frequency[key] = 1
            frequency_list[1][key] = None
            min_freq = 1
            return result

        return wrapper

    return decorator