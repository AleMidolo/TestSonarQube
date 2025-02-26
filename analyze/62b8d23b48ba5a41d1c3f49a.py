from collections import OrderedDict
from functools import wraps

def mru_cache(maxsize=128, typed=False):
    """
    Decorador para envolver una función con un objeto invocable que memoriza hasta `maxsize` resultados basados en un algoritmo de Más Recientemente Usado (MRU).
    """
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