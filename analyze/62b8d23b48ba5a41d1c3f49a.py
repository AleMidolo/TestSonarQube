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
            
            try:
                # Try to get from cache
                result = cache[key]
                # Update access order
                order.remove(key)
                order.append(key)
                return result
                
            except KeyError:
                # Calculate result
                result = func(*args, **kwargs)
                
                # Add to cache
                cache[key] = result
                order.append(key)
                
                # Remove oldest if cache too large
                if len(cache) > maxsize:
                    oldest = order.pop(0)
                    del cache[oldest]
                    
                return result
                
        wrapper.cache_info = lambda: {
            'maxsize': maxsize,
            'currsize': len(cache),
            'hits': len(order),
            'misses': func.__code__.co_firstlineno
        }
        
        wrapper.cache_clear = lambda: cache.clear() or order.clear()
        
        return wrapper
        
    return decorator