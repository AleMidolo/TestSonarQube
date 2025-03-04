def cached(cache, key=hashkey, lock=None):
    """
    Decorator to wrap a function with a memoizing callable that saves
    results in a cache.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            k = key(*args, **kwargs)
            
            try:
                # Try to get result from cache first
                result = cache[k]
                return result
            except KeyError:
                # If not in cache, compute and store result
                if lock is not None:
                    with lock:
                        result = func(*args, **kwargs)
                        cache[k] = result
                else:
                    result = func(*args, **kwargs)
                    cache[k] = result
                return result
                
        return wrapper
    return decorator