import time
from functools import wraps, lru_cache

def ttl_cache(maxsize=128, ttl=600, timer=time.monotonic, typed=False):
    """
    Decorator to wrap a function with a memoizing callable that saves
    up to `maxsize` results based on a Least Recently Used (LRU)
    algorithm with a per-item time-to-live (TTL) value.
    """
    def decorator(func):
        @lru_cache(maxsize=maxsize, typed=typed)
        def cached_func(*args, **kwargs):
            return func(*args, **kwargs)

        @wraps(func)
        def wrapper(*args, **kwargs):
            key = (args, frozenset(kwargs.items())) if typed else (args, frozenset(kwargs.items()))
            if key in wrapper._cache_info:
                value, timestamp = wrapper._cache_info[key]
                if timer() - timestamp < ttl:
                    return value
            result = cached_func(*args, **kwargs)
            wrapper._cache_info[key] = (result, timer())
            return result

        wrapper._cache_info = {}
        return wrapper
    return decorator