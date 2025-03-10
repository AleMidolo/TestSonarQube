import time
from functools import lru_cache, wraps

def ttl_cache(maxsize=128, ttl=600, timer=time.monotonic, typed=False):
    """
    Decorador para envolver una función con una llamada que memoriza y guarda
    hasta `maxsize` resultados, utilizando un algoritmo de "Menos Usado Recientemente" (Least Recently Used, LRU) con un valor de tiempo de vida (TTL, Time-To-Live) por elemento.
    """
    def decorator(func):
        @lru_cache(maxsize=maxsize, typed=typed)
        def cached_func(*args, **kwargs):
            return func(*args, **kwargs)

        @wraps(func)
        def wrapper(*args, **kwargs):
            key = (args, frozenset(kwargs.items())) if typed else (args, tuple(kwargs.items()))
            if key in wrapper._cache:
                value, timestamp = wrapper._cache[key]
                if timer() - timestamp < ttl:
                    return value
            value = cached_func(*args, **kwargs)
            wrapper._cache[key] = (value, timer())
            return value

        wrapper._cache = {}
        return wrapper

    return decorator