import time
from collections import OrderedDict
from functools import wraps

def ttl_cache(maxsize=128, ttl=600, timer=time.monotonic, typed=False):
    def decorator(func):
        cache = OrderedDict()
        timestamps = {}

        @wraps(func)
        def wrapper(*args, **kwargs):
            key = args if not typed else (args, frozenset(kwargs.items()))
            current_time = timer()

            # Clean up expired items
            if key in cache:
                if current_time - timestamps[key] < ttl:
                    return cache[key]
                else:
                    del cache[key]
                    del timestamps[key]

            # If cache is full, remove the oldest item
            if len(cache) >= maxsize:
                cache.popitem(last=False)

            # Call the function and store the result
            result = func(*args, **kwargs)
            cache[key] = result
            timestamps[key] = current_time
            return result

        return wrapper

    return decorator