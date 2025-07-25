from functools import wraps
from collections import OrderedDict

def mru_cache(maxsize=128, typed=False):
    """
    Decorator per racchiudere una funzione con un oggetto richiamabile che memorizza
    fino a `maxsize` risultati basandosi su un algoritmo di tipo Most Recently Used (MRU).
    """
    def decorator(func):
        cache = OrderedDict()

        @wraps(func)
        def wrapper(*args, **kwargs):
            if typed:
                key = (args, tuple(sorted(kwargs.items())))
            else:
                key = args + tuple(sorted(kwargs.items()))

            if key in cache:
                # Move the accessed key to the end to mark it as most recently used
                cache.move_to_end(key)
                return cache[key]

            result = func(*args, **kwargs)
            cache[key] = result

            if len(cache) > maxsize:
                # Remove the least recently used item
                cache.popitem(last=False)

            return result

        return wrapper

    return decorator