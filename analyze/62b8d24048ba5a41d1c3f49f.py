import time
from collections import OrderedDict
from functools import wraps

def ttl_cache(maxsize=128, ttl=600, timer=time.monotonic, typed=False):
    """
    Decorator to wrap a function with a memoizing callable that saves
    up to `maxsize` results based on a Least Recently Used (LRU)
    algorithm with a per-item time-to-live (TTL) value.
    """
    def decorator(func):
        cache = OrderedDict()
        
        @wraps(func)
        def wrapper(*args, **kwargs):
            key = args if not typed else (type(arg).__name__ for arg in args)
            current_time = timer()
            if key in cache:
                value, timestamp = cache[key]
                if current_time - timestamp < ttl:
                    cache.move_to_end(key)  # Mark as recently used
                    return value
                else:
                    del cache[key]  # Remove expired item
            
            # Call the function and cache the result
            value = func(*args, **kwargs)
            cache[key] = (value, current_time)
            if len(cache) > maxsize:
                cache.popitem(last=False)  # Remove the oldest item
            return value
        
        return wrapper
    
    return decorator