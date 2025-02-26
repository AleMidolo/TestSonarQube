import time
import functools
from collections import OrderedDict

def ttl_cache(maxsize=128, ttl=600, timer=time.monotonic, typed=False):
    """
    Decorator to wrap a function with a memoizing callable that saves
    up to `maxsize` results based on a Least Recently Used (LRU)
    algorithm with a per-item time-to-live (TTL) value.
    """
    def decorator(func):
        cache = OrderedDict()
        
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            key = args if not typed else (args, frozenset(kwargs.items()))
            current_time = timer()
            
            # Clean up expired items
            if key in cache:
                value, timestamp = cache[key]
                if current_time - timestamp < ttl:
                    cache.move_to_end(key)
                    return value
                else:
                    del cache[key]
            
            # Call the function and cache the result
            value = func(*args, **kwargs)
            cache[key] = (value, current_time)
            
            # Maintain the cache size
            if len(cache) > maxsize:
                cache.popitem(last=False)
                
            return value
        
        return wrapper
    
    return decorator