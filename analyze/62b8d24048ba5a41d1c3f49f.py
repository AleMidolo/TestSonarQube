import time
from functools import lru_cache, wraps

def ttl_cache(maxsize=128, ttl=600, timer=time.monotonic, typed=False):
    def decorator(func):
        @lru_cache(maxsize=maxsize, typed=typed)
        def cached_func(*args, **kwargs):
            value, last_update = func(*args, **kwargs)
            if timer() - last_update > ttl:
                cached_func.cache_clear()
                value, last_update = func(*args, **kwargs)
            return value

        @wraps(func)
        def wrapper(*args, **kwargs):
            return cached_func(*args, **kwargs)

        return wrapper
    return decorator