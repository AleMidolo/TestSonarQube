from functools import wraps
from collections import OrderedDict
import time

def ttl_cache(maxsize=128, ttl=600, timer=time.monotonic, typed=False):
    """
    Decorator to wrap a function with a memoizing callable that saves
    up to `maxsize` results based on a Least Recently Used (LRU)
    algorithm with a per-item time-to-live (TTL) value.
    """
    def decorator(func):
        # Create cache as ordered dictionary
        cache = OrderedDict()
        
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Create cache key based on arguments
            key = str(args)
            if kwargs:
                key += str(sorted(kwargs.items()))
            if typed:
                key += str(tuple(type(arg) for arg in args))
                if kwargs:
                    key += str(tuple(type(val) for val in kwargs.values()))
                    
            # Get current time
            now = timer()
            
            # Check if key exists and hasn't expired
            if key in cache:
                result, timestamp = cache[key]
                if now - timestamp <= ttl:
                    # Move to end (most recently used)
                    cache.move_to_end(key)
                    return result
                else:
                    # Remove expired item
                    del cache[key]
                    
            # Compute new result
            result = func(*args, **kwargs)
            
            # Add to cache
            cache[key] = (result, now)
            
            # Remove oldest items if cache is too large
            while len(cache) > maxsize:
                cache.popitem(last=False)
                
            return result
            
        # Add cache clear method
        wrapper.cache_clear = cache.clear
        
        return wrapper
    return decorator