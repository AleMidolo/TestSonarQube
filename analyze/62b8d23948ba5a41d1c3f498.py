def lru_cache(maxsize=128, typed=False):
    """Decorador para envolver una función con un objeto invocable que memoriza
    hasta `maxsize` resultados basados en un algoritmo de Menor Recientemente Usado (LRU, por sus siglas en inglés).
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

        wrapper.cache_clear = cache.clear
        wrapper.cache_info = lambda: (len(cache), maxsize)
        return wrapper

    return decorator