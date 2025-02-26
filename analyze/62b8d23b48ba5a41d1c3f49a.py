def mru_cache(maxsize=128, typed=False):
    """
    Decorator per racchiudere una funzione con un oggetto richiamabile che memorizza
    fino a `maxsize` risultati basandosi su un algoritmo di tipo Most Recently Used (MRU).
    """
    from collections import OrderedDict
    from functools import wraps

    def decorator(func):
        cache = OrderedDict()

        @wraps(func)
        def wrapper(*args, **kwargs):
            key = (args, frozenset(kwargs.items())) if typed else args
            if key in cache:
                # Move the accessed item to the end to mark it as recently used
                cache.move_to_end(key)
                return cache[key]
            result = func(*args, **kwargs)
            cache[key] = result
            if len(cache) > maxsize:
                # Pop the first item (the least recently used)
                cache.popitem(last=False)
            return result

        return wrapper

    return decorator