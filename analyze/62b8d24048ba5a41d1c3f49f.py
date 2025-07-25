import time
from collections import OrderedDict
from functools import wraps

def ttl_cache(maxsize=128, ttl=600, timer=time.monotonic, typed=False):
    """
    Decorator per racchiudere una funzione con un oggetto callable di memorizzazione (memoization) 
    che salva fino a `maxsize` risultati basandosi su un algoritmo Least Recently Used (LRU) 
    con un valore di time-to-live (TTL) per ogni elemento.
    """
    def decorator(func):
        cache = OrderedDict()
        cache_times = {}

        @wraps(func)
        def wrapper(*args, **kwargs):
            key = args if not typed else (args, frozenset(kwargs.items()))
            current_time = timer()

            # Invalidate expired cache entries
            if key in cache:
                if current_time - cache_times[key] < ttl:
                    # Move to end to show that it was recently used
                    cache.move_to_end(key)
                    return cache[key]
                else:
                    # Remove expired entry
                    del cache[key]
                    del cache_times[key]

            # Call the function and cache the result
            result = func(*args, **kwargs)
            cache[key] = result
            cache_times[key] = current_time

            # Maintain the cache size
            if len(cache) > maxsize:
                cache.popitem(last=False)  # Remove the first (oldest) item

            return result

        return wrapper

    return decorator