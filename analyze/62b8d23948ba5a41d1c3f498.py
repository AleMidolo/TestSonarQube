from collections import OrderedDict
from functools import wraps

def lru_cache(maxsize=128, typed=False):
    def decorator(func):
        # Create ordered dictionary to store cached results
        cache = OrderedDict()
        
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Create cache key based on args and kwargs
            # Include types in key if typed=True
            if typed:
                key = (tuple(type(arg) for arg in args),
                      tuple(args),
                      tuple(sorted(kwargs.items())),
                      tuple(type(v) for v in kwargs.values()))
            else:
                key = (args, tuple(sorted(kwargs.items())))
            
            # Return cached result if it exists
            if key in cache:
                # Move to end to mark as most recently used
                cache.move_to_end(key)
                return cache[key]
            
            # Calculate new result
            result = func(*args, **kwargs)
            
            # Add to cache, remove oldest item if at maxsize
            cache[key] = result
            if len(cache) > maxsize:
                cache.popitem(last=False)
                
            return result
            
        # Add cache info method
        wrapper.cache_info = lambda: {
            'maxsize': maxsize,
            'currsize': len(cache),
            'hits': sum(1 for _ in cache.values()),
            'misses': wrapper.calls - sum(1 for _ in cache.values())
        }
        
        # Add clear cache method
        wrapper.cache_clear = cache.clear
        
        # Initialize call counter
        wrapper.calls = 0
        
        return wrapper
    return decorator