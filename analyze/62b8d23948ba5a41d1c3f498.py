from collections import OrderedDict
from functools import wraps

def lru_cache(maxsize=128, typed=False):
    def decorator(func):
        # Create ordered dictionary to store cache
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
            
            # Calculate result
            result = func(*args, **kwargs)
            
            # Add to cache
            cache[key] = result
            
            # Remove oldest item if cache is full
            if maxsize and len(cache) > maxsize:
                cache.popitem(last=False)
                
            return result
            
        # Add cache info method
        def cache_info():
            hits = sum(1 for k in cache)
            return {
                'hits': hits,
                'misses': wrapper.calls - hits,
                'maxsize': maxsize,
                'currsize': len(cache)
            }
            
        wrapper.cache = cache
        wrapper.cache_info = cache_info
        wrapper.calls = 0
        
        return wrapper
    return decorator