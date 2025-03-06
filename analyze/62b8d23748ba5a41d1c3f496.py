from functools import wraps
from collections import defaultdict, OrderedDict

def lfu_cache(maxsize=128, typed=False):
    def decorator(func):
        cache = {}
        freq = defaultdict(OrderedDict)
        min_freq = 0

        @wraps(func)
        def wrapper(*args, **kwargs):
            if typed:
                key = (args, tuple(sorted(kwargs.items())))
            else:
                key = args + tuple(sorted(kwargs.items()))

            if key in cache:
                # Update frequency
                freq_val = cache[key][1]
                del freq[freq_val][key]
                if not freq[freq_val]:
                    del freq[freq_val]
                    if min_freq == freq_val:
                        min_freq += 1
                freq[freq_val + 1][key] = None
                cache[key][1] += 1
                return cache[key][0]
            else:
                result = func(*args, **kwargs)
                if len(cache) >= maxsize:
                    # Remove the least frequently used item
                    lfu_key = next(iter(freq[min_freq]))
                    del cache[lfu_key]
                    del freq[min_freq][lfu_key]
                    if not freq[min_freq]:
                        del freq[min_freq]
                cache[key] = [result, 1]
                freq[1][key] = None
                min_freq = 1
                return result

        return wrapper

    return decorator