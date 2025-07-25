def mru_cache(maxsize=128, typed=False):
    """
    Decorator to wrap a function with a memoizing callable that saves
    up to `maxsize` results based on a Most Recently Used (MRU)
    algorithm.
    """
    def decorator(func):
        # Store cache and order of access
        cache = {}
        access_order = []
        
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
                # Move accessed item to front of access order
                access_order.remove(key)
                access_order.append(key)
                return cache[key]
                
            result = func(*args, **kwargs)
            
            if len(cache) >= maxsize:
                # Remove least recently used item
                lru_key = access_order.pop(0)
                del cache[lru_key]
                
            # Add new result to cache
            cache[key] = result
            access_order.append(key)
            
            return result
            
        wrapper.cache_info = lambda: {
            'maxsize': maxsize,
            'currsize': len(cache),
            'cache': cache,
            'access_order': access_order
        }
        
        wrapper.cache_clear = lambda: (cache.clear(), access_order.clear())
        
        return wrapper
        
    return decorator