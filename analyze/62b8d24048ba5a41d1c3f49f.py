import time
from functools import wraps
from collections import OrderedDict

def ttl_cache(maxsize=128, ttl=600, timer=time.monotonic, typed=False):
    def decorator(func):
        cache = OrderedDict()
        @wraps(func)
        def wrapper(*args, **kwargs):
            if typed:
                key = (args, tuple((k, type(v)) for k, v in sorted(kwargs.items())))
            else:
                key = (args, tuple(sorted(kwargs.items())))
            
            current_time = timer()
            
            if key in cache:
                result, timestamp = cache[key]
                if current_time - timestamp <= ttl:
                    # Move the accessed item to the end to mark it as recently used
                    cache.move_to_end(key)
                    return result
                else:
                    # Remove expired item
                    del cache[key]
            
            result = func(*args, **kwargs)
            cache[key] = (result, current_time)
            
            if len(cache) > maxsize:
                # Remove the least recently used item
                cache.popitem(last=False)
            
            return result
        return wrapper
    return decorator