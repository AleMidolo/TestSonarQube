from functools import wraps
from collections import defaultdict, OrderedDict

def lfu_cache(maxsize=128, typed=False):
    """
    Decorator per racchiudere una funzione con un oggetto callable di memoizzazione
    che salva fino a `maxsize` risultati basandosi su un algoritmo Least Frequently Used (LFU).
    """
    def decorator(func):
        cache = {}
        freq = defaultdict(OrderedDict)
        min_freq = 0

        @wraps(func)
        def wrapper(*args, **kwargs):
            if typed:
                key = (args, tuple(sorted(kwargs.items())))
            else:
                key = (args, frozenset(kwargs.items()))

            if key in cache:
                # Increment frequency and move to the next frequency level
                freq_val = cache[key][1]
                del freq[freq_val][key]
                if not freq[freq_val]:
                    del freq[freq_val]
                    if freq_val == min_freq:
                        min_freq += 1
                freq_val += 1
                freq[freq_val][key] = None
                cache[key] = (cache[key][0], freq_val)
                return cache[key][0]

            result = func(*args, **kwargs)

            if len(cache) >= maxsize:
                # Remove the least frequently used item
                evict_key, _ = freq[min_freq].popitem(last=False)
                if not freq[min_freq]:
                    del freq[min_freq]
                del cache[evict_key]

            cache[key] = (result, 1)
            freq[1][key] = None
            min_freq = 1

            return result

        return wrapper

    return decorator