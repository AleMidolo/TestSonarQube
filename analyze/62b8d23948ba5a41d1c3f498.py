from functools import wraps

def lru_cache(maxsize=128, typed=False):
    def decorator(func):
        cache = {}
        order = []

        @wraps(func)
        def wrapper(*args, **kwargs):
            key = args if not typed else (args, frozenset(kwargs.items()))
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

        return wrapper
    return decorator