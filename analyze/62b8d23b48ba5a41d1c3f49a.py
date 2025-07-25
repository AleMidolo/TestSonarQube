from functools import wraps

def mru_cache(maxsize=128, typed=False):
    """
    Decorator to wrap a function with a memoizing callable that saves
    up to `maxsize` results based on a Most Recently Used (MRU)
    algorithm.
    """
    cache = {}
    order = []

    @wraps(func)
    def wrapper(func):
        @wraps(func)
        def wrapped(*args, **kwargs):
            key = (args, frozenset(kwargs.items())) if typed else args
            if key in cache:
                order.remove(key)
                order.append(key)
                return cache[key]
            result = func(*args, **kwargs)
            if len(cache) >= maxsize:
                oldest = order.pop(0)
                del cache[oldest]
            cache[key] = result
            order.append(key)
            return result

        return wrapped

    return wrapper