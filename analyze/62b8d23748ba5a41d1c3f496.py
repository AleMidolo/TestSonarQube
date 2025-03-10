from functools import wraps
from collections import defaultdict, OrderedDict

def lfu_cache(maxsize=128, typed=False):
    """
    Decorator per racchiudere una funzione con un oggetto callable di memoizzazione
    che salva fino a `maxsize` risultati basandosi su un algoritmo Least Frequently Used (LFU).
    """
    def decorator(func):
        cache = {}
        frequency = defaultdict(int)
        freq_map = defaultdict(OrderedDict)
        min_freq = 0

        @wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal min_freq
            key = args + tuple(sorted(kwargs.items())) if typed else args + tuple(kwargs.items())
            if key in cache:
                # Increment frequency
                freq = frequency[key]
                frequency[key] += 1
                # Remove from current frequency map
                del freq_map[freq][key]
                # Add to new frequency map
                freq_map[freq + 1][key] = None
                # Update min_freq if necessary
                if freq == min_freq and not freq_map[freq]:
                    min_freq += 1
                return cache[key]
            # If cache is full, evict the least frequently used item
            if len(cache) >= maxsize:
                evict_key, _ = freq_map[min_freq].popitem(last=False)
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