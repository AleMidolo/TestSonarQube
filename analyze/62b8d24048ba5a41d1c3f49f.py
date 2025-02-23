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
            key = args if not typed else (type(arg).__name__ for arg in args)
            if key in cache:
                if timer() - cache_times[key] < ttl:
                    cache.move_to_end(key)
                    return cache[key]
                else:
                    del cache[key]
                    del cache_times[key]

            result = func(*args, **kwargs)
            cache[key] = result
            cache_times[key] = timer()

            if len(cache) > maxsize:
                cache.popitem(last=False)
                cache_times.popitem(last=False)

            return result

        return wrapper

    return decorator