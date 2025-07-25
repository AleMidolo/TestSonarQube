from functools import wraps
from collections import defaultdict, OrderedDict

def lfu_cache(maxsize=128, typed=False):
    def decorator(func):
        cache = {}
        frequency = defaultdict(int)
        frequency_lists = defaultdict(OrderedDict)
        min_frequency = 0

        @wraps(func)
        def wrapper(*args, **kwargs):
            if typed:
                key = (args, tuple(sorted(kwargs.items())))
            else:
                key = args + tuple(sorted(kwargs.items()))

            if key in cache:
                # Increment the frequency of the key
                frequency[key] += 1
                # Move the key to the new frequency list
                frequency_lists[frequency[key] - 1].pop(key)
                frequency_lists[frequency[key]][key] = None
                # Update min_frequency if necessary
                if not frequency_lists[min_frequency]:
                    min_frequency += 1
                return cache[key]

            # If the cache is full, evict the least frequently used item
            if len(cache) >= maxsize:
                evict_key = next(iter(frequency_lists[min_frequency]))
                frequency_lists[min_frequency].pop(evict_key)
                del cache[evict_key]
                del frequency[evict_key]

            # Add the new item to the cache
            result = func(*args, **kwargs)
            cache[key] = result
            frequency[key] = 1
            frequency_lists[1][key] = None
            min_frequency = 1
            return result

        return wrapper
    return decorator