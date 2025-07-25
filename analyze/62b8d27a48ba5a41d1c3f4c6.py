def cached(cache, key=hashkey, lock=None):
    """
    Decorator to wrap a function with a memoizing callable that saves
    results in a cache.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            k = key(*args, **kwargs)
            
            try:
                # Try to get result from cache
                result = cache[k]
                return result
            except KeyError:
                # Key not found, need to compute result
                if lock is not None:
                    with lock:
                        # Check cache again in case another thread computed result
                        if k in cache:
                            return cache[k]
                        result = func(*args, **kwargs)
                        cache[k] = result
                else:
                    # No lock needed, just compute and cache result
                    result = func(*args, **kwargs)
                    cache[k] = result
                    
                return result
                
        return wrapper
    return decorator