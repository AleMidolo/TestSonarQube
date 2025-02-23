import time
import functools
from collections import OrderedDict

def ttl_cache(maxsize=128, ttl=600, timer=time.monotonic, typed=False):
    """Decorator to wrap a function with a memoizing callable that saves
    up to `maxsize` results based on a Least Recently Used (LRU)
    algorithm with a per-item time-to-live (TTL) value.
    """
    def decorator(func):
        cache = OrderedDict()
        cache_expiry = {}

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            key = args if not typed else (type(arg).__name__ for arg in args)
            if key in cache:
                if timer() - cache_expiry[key] < ttl:
                    cache.move_to_end(key)
                    return cache[key]
                else:
                    del cache[key]
                    del cache_expiry[key]

            result = func(*args, **kwargs)
            cache[key] = result
            cache_expiry[key] = timer()

            if len(cache) > maxsize:
                cache.popitem(last=False)
                cache_expiry.popitem(last=False)

            return result

        return wrapper

    return decorator