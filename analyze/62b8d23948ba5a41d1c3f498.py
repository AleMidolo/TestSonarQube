from functools import wraps
from collections import OrderedDict

def lru_cache(maxsize=128, typed=False):
    """Decorator to wrap a function with a memoizing callable that saves
    up to `maxsize` results based on a Least Recently Used (LRU)
    algorithm."""
    
    def decorator(func):
        cache = OrderedDict()
        
        @wraps(func)
        def wrapper(*args, **kwargs):
            key = args if not typed else (args, frozenset(kwargs.items()))
            if key in cache:
                cache.move_to_end(key)
                return cache[key]
            result = func(*args, **kwargs)
            cache[key] = result
            if len(cache) > maxsize:
                cache.popitem(last=False)
            return result
        
        wrapper.cache_clear = cache.clear
        wrapper.cache_info = lambda: (len(cache), maxsize)
        return wrapper
    
    return decorator