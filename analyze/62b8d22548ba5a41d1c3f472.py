def cachedmethod(cache, key=hashkey, lock=None):
    """
    Decorator to wrap a class or instance method with a memoizing
    callable that saves results in a cache.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Create a unique cache key based on the method and its arguments
            cache_key = key(func, *args, **kwargs)
            if lock:
                with lock:
                    if cache_key in cache:
                        return cache[cache_key]
                    result = func(*args, **kwargs)
                    cache[cache_key] = result
                    return result
            else:
                if cache_key in cache:
                    return cache[cache_key]
                result = func(*args, **kwargs)
                cache[cache_key] = result
                return result
        return wrapper
    return decorator