def lru_cache(maxsize=128, typed=False):
    def decorator(func):
        # Create cache dictionary and order list
        cache = {}
        order = []
        
        def wrapper(*args, **kwargs):
            # Create cache key based on args and kwargs
            key = str(args) + str(kwargs)
            if typed:
                key += str([type(arg) for arg in args])
                key += str([type(val) for val in kwargs.values()])
                
            # Return cached result if exists
            if key in cache:
                # Move key to end of order list since it was just used
                order.remove(key)
                order.append(key)
                return cache[key]
                
            # Calculate new result
            result = func(*args, **kwargs)
            
            # Add to cache
            cache[key] = result
            order.append(key)
            
            # Remove oldest item if cache is full
            if len(cache) > maxsize:
                oldest_key = order.pop(0)
                del cache[oldest_key]
                
            return result
            
        # Add cache info method
        def cache_info():
            return {
                'hits': len(order),
                'misses': func.__code__.co_firstlineno,
                'maxsize': maxsize,
                'currsize': len(cache)
            }
            
        wrapper.cache_info = cache_info
        
        # Add cache clear method
        def cache_clear():
            cache.clear()
            order.clear()
            
        wrapper.cache_clear = cache_clear
        
        return wrapper
        
    # Handle no arguments case
    if callable(maxsize):
        func = maxsize
        maxsize = 128
        return decorator(func)
        
    return decorator