from functools import wraps
from collections import OrderedDict
import time

def ttl_cache(maxsize=128, ttl=600, timer=time.monotonic, typed=False):
    def decorator(func):
        # Create cache as OrderedDict to maintain LRU order
        cache = OrderedDict()
        
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Create cache key based on args and typed flag
            key = str(args) + str(kwargs)
            if typed:
                key += str(tuple(type(arg) for arg in args))
                key += str(tuple(type(val) for val in kwargs.values()))
                
            # Get current time
            now = timer()
            
            # Check if key exists and hasn't expired
            if key in cache:
                result, timestamp = cache[key]
                if now - timestamp <= ttl:
                    # Move to end to mark as most recently used
                    cache.move_to_end(key)
                    return result
                else:
                    # Remove expired entry
                    del cache[key]
                    
            # Compute new result
            result = func(*args, **kwargs)
            
            # Add to cache
            cache[key] = (result, now)
            
            # Remove oldest entries if cache is too large
            while len(cache) > maxsize:
                cache.popitem(last=False)
                
            return result
            
        # Add clear method to wrapper
        wrapper.cache_clear = cache.clear
        
        return wrapper
    return decorator