import time
from functools import lru_cache, wraps

def ttl_cache(maxsize=128, ttl=600, timer=time.monotonic, typed=False):
    def decorator(func):
        cache = lru_cache(maxsize=maxsize, typed=typed)(func)
        cache.expire_times = {}

        @wraps(func)
        def wrapped(*args, **kwargs):
            key = args + (tuple(sorted(kwargs.items())),) if kwargs else args
            current_time = timer()
            if key in cache.expire_times and current_time >= cache.expire_times[key]:
                cache.cache_clear()
                cache.expire_times.pop(key, None)
            if key not in cache.expire_times:
                cache.expire_times[key] = current_time + ttl
            return cache(*args, **kwargs)
        return wrapped
    return decorator