def mru_cache(maxsize=128, typed=False):
    """
    Decorator to wrap a function with a memoizing callable that saves
    up to `maxsize` results based on a Most Recently Used (MRU)
    algorithm.
    """
    def decorator(func):
        # Store cache and order of keys
        cache = {}
        key_order = []
        
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
                # Move key to end (most recently used)
                key_order.remove(key)
                key_order.append(key)
                return result
                
            except KeyError:
                # Calculate result
                result = func(*args, **kwargs)
                
                # Add to cache
                cache[key] = result
                key_order.append(key)
                
                # Remove oldest if cache too large
                if len(cache) > maxsize:
                    oldest_key = key_order.pop(0)
                    del cache[oldest_key]
                    
                return result
                
        wrapper.cache_info = lambda: {
            'maxsize': maxsize,
            'currsize': len(cache),
            'cache': cache,
            'order': key_order
        }
        
        wrapper.cache_clear = lambda: cache.clear() or key_order.clear()
        
        return wrapper
        
    return decorator