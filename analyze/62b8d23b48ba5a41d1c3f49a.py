def mru_cache(maxsize=128, typed=False):
    from collections import OrderedDict
    from functools import wraps

    def decorator(func):
        cache = OrderedDict()

        @wraps(func)
        def wrapper(*args, **kwargs):
            key = (args, frozenset(kwargs.items())) if typed else args
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