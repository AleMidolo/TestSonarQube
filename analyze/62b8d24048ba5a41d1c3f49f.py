import time
from functools import wraps, lru_cache

def ttl_cache(maxsize=128, ttl=600, timer=time.monotonic, typed=False):
    """
    Decorator to wrap a function with a memoizing callable that saves
    up to `maxsize` results based on a Least Recently Used (LRU)
    algorithm with a per-item time-to-live (TTL) value.
    """
    def decorator(func):
        cache = {}

        @wraps(func)
        def wrapped(*args, **kwargs):
            key = args + tuple(sorted(kwargs.items())) if typed else args + tuple(sorted(kwargs.items()))
            current_time = timer()
            if key in cache:
                result, timestamp = cache[key]
                if current_time - timestamp < ttl:
                    return result
            result = func(*args, **kwargs)
            cache[key] = (result, current_time)
            if len(cache) > maxsize:
                oldest_key = min(cache.keys(), key=lambda k: cache[k][1])
                del cache[oldest_key]
            return result

        return wrapped

    return decorator