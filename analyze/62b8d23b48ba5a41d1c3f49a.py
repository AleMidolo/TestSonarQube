def mru_cache(maxsize=128, typed=False):
    """
    Decorator to wrap a function with a memoizing callable that saves
    up to `maxsize` results based on a Most Recently Used (MRU)
    algorithm.
    """
    def decorator(func):
        # Store cache and order of usage
        cache = {}
        order = []
        
        def make_key(args, kwargs):
            # Create cache key from arguments
            key = (args, frozenset(kwargs.items()))
            if typed:
                # Add types to key if typed=True
                key += tuple(type(arg) for arg in args)
                key += tuple(type(val) for val in kwargs.values())
            return hash(key)
        
        def wrapper(*args, **kwargs):
            key = make_key(args, kwargs)
            
            if key in cache:
                # Move accessed item to front of order
                order.remove(key)
                order.append(key)
                return cache[key]
                
            result = func(*args, **kwargs)
            
            if len(cache) >= maxsize:
                # Remove least recently used item
                lru_key = order.pop(0)
                del cache[lru_key]
                
            # Add new result to cache
            cache[key] = result
            order.append(key)
            
            return result
            
        return wrapper
        
    return decorator