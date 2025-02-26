def cached(cache, key=hashkey, lock=None):
    """
    Decorator to wrap a function with a memoizing callable that saves
    results in a cache.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Create a unique cache key based on the function arguments
            cache_key = key(*args, **kwargs)
            if cache_key in cache:
                return cache[cache_key]
            with (lock or dummy_lock):
                if cache_key not in cache:  # Double-check in case another thread added it
                    cache[cache_key] = func(*args, **kwargs)
            return cache[cache_key]
        return wrapper
    return decorator