import time
from collections import OrderedDict
from functools import wraps

def ttl_cache(maxsize=128, ttl=600, timer=time.monotonic, typed=False):
    def decorator(func):
        cache = OrderedDict()
        timestamps = {}

        @wraps(func)
        def wrapper(*args, **kwargs):
            key = args if not typed else (type(arg) for arg in args)
            if key in cache:
                if timer() - timestamps[key] < ttl:
                    return cache[key]
                else:
                    del cache[key]
                    del timestamps[key]
            result = func(*args, **kwargs)
            cache[key] = result
            timestamps[key] = timer()
            if len(cache) > maxsize:
                cache.popitem(last=False)
            return result

        return wrapper

    return decorator