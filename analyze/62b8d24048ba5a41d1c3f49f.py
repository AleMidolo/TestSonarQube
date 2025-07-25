from functools import wraps
from collections import OrderedDict
import time

def ttl_cache(maxsize=128, ttl=600, timer=time.monotonic, typed=False):
    def decorator(func):
        # Create cache as ordered dictionary
        cache = OrderedDict()
        
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Create cache key based on args
            key = str(args)
            if typed:
                key += str(type(args))
            if kwargs:
                key += str(sorted(kwargs.items()))
                if typed:
                    key += str(type(kwargs))
                    
            now = timer()
            
            # Check if key exists and hasn't expired
            if key in cache:
                result, timestamp = cache[key]
                if now - timestamp <= ttl:
                    # Move to end to mark as recently used
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
        def clear_cache():
            cache.clear()
            
        wrapper.clear_cache = clear_cache
        return wrapper
        
    return decorator