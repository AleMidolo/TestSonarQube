import time
from collections import OrderedDict
from functools import wraps

def ttl_cache(maxsize=128, ttl=600, timer=time.monotonic, typed=False):
    """
    Decorador para envolver una función con una llamada que memoriza y guarda
    hasta `maxsize` resultados, utilizando un algoritmo de "Menos Usado Recientemente" (Least Recently Used, LRU) con un valor de tiempo de vida (TTL, Time-To-Live) por elemento.
    """
    def decorator(func):
        cache = OrderedDict()
        timestamps = {}

        @wraps(func)
        def wrapper(*args, **kwargs):
            key = args if not typed else (args, frozenset(kwargs.items()))
            current_time = timer()

            # Clean up expired items
            if key in cache:
                if current_time - timestamps[key] < ttl:
                    cache.move_to_end(key)
                    return cache[key]
                else:
                    del cache[key]
                    del timestamps[key]

            # Call the function and cache the result
            result = func(*args, **kwargs)
            cache[key] = result
            timestamps[key] = current_time

            # Maintain the cache size
            if len(cache) > maxsize:
                cache.popitem(last=False)
                timestamps.popitem(last=False)

            return result

        return wrapper

    return decorator