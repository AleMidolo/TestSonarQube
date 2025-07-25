import time
from functools import wraps, lru_cache

def ttl_cache(maxsize=128, ttl=600, timer=time.monotonic, typed=False):
    def decorator(func):
        @lru_cache(maxsize=maxsize, typed=typed)
        def cached_func(*args, **kwargs):
            return func(*args, **kwargs)

        @wraps(func)
        def wrapper(*args, **kwargs):
            key = (args, frozenset(kwargs.items()))
            if key in wrapper._cache:
                value, timestamp = wrapper._cache[key]
                if timer() - timestamp < ttl:
                    return value
            result = cached_func(*args, **kwargs)
            wrapper._cache[key] = (result, timer())
            return result

        wrapper._cache = {}
        return wrapper
    return decorator