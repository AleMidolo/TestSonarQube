from functools import wraps
from collections import OrderedDict

def mru_cache(maxsize=128, typed=False):
    """
    Decorador para envolver una función con un objeto invocable que memoriza hasta `maxsize` resultados basados en un algoritmo de Más Recientemente Usado (MRU).
    """
    def decorator(func):
        cache = OrderedDict()
        
        @wraps(func)
        def wrapper(*args, **kwargs):
            if typed:
                key = (args, tuple((k, type(v)) for k, v in sorted(kwargs.items()))
            else:
                key = (args, tuple(sorted(kwargs.items())))
            
            if key in cache:
                # Move the accessed key to the end to mark it as recently used
                cache.move_to_end(key)
                return cache[key]
            
            result = func(*args, **kwargs)
            
            if len(cache) >= maxsize:
                # Remove the least recently used item
                cache.popitem(last=False)
            
            cache[key] = result
            return result
        
        return wrapper
    
    return decorator