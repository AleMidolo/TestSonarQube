def lru_cache(maxsize=128, typed=False):
    """
    Decorator per racchiudere una funzione con un oggetto callable che memorizza
    fino a `maxsize` risultati basandosi su un algoritmo Least Recently Used (LRU).
    """
    from collections import OrderedDict
    from functools import wraps

    def decorator(func):
        cache = OrderedDict()

        @wraps(func)
        def wrapper(*args, **kwargs):
            key = args if not typed else (args, frozenset(kwargs.items()))
            if key in cache:
                cache.move_to_end(key)
                return cache[key]
            result = func(*args, **kwargs)
            cache[key] = result
            if len(cache) > maxsize:
                cache.popitem(last=False)
            return result

        return wrapper

    return decorator