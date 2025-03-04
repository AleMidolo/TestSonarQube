def mru_cache(maxsize=128, typed=False):
    def decorator(func):
        from functools import wraps
        from collections import OrderedDict

        # Create cache dictionary
        cache = OrderedDict()

        @wraps(func)
        def wrapper(*args, **kwargs):
            # Create cache key based on arguments
            if typed:
                key = (tuple(args), tuple(sorted(kwargs.items())), 
                      tuple(type(arg) for arg in args),
                      tuple(type(val) for val in kwargs.values()))
            else:
                key = (tuple(args), tuple(sorted(kwargs.items())))

            # Check if result is in cache
            if key in cache:
                # Move to end since it was most recently used
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
            return {
                'maxsize': maxsize,
                'currsize': len(cache),
                'hits': sum(1 for _ in cache),
                'typed': typed
            }
        wrapper.cache_info = cache_info

        # Add cache clear method
        def cache_clear():
            cache.clear()
        wrapper.cache_clear = cache_clear

        return wrapper

    # Handle direct decoration with no arguments
    if callable(maxsize):
        func = maxsize
        maxsize = 128
        return decorator(func)
    
    return decorator