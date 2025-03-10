import time
from functools import lru_cache, wraps

def ttl_cache(maxsize=128, ttl=600, timer=time.monotonic, typed=False):
    def decorator(func):
        @lru_cache(maxsize=maxsize, typed=typed)
        def cached_func(*args, **kwargs):
            return func(*args, **kwargs)

        @wraps(func)
        def wrapper(*args, **kwargs):
            key = (args, frozenset(kwargs.items())) if typed else (args, tuple(kwargs.items()))
            current_time = timer()
            if key in wrapper._cache_info:
                last_access_time, result = wrapper._cache_info[key]
                if current_time - last_access_time < ttl:
                    wrapper._cache_info[key] = (current_time, result)
                    return result
                else:
                    del wrapper._cache_info[key]
            result = cached_func(*args, **kwargs)
            wrapper._cache_info[key] = (current_time, result)
            return result

        wrapper._cache_info = {}
        return wrapper
    return decorator