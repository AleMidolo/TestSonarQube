from functools import wraps

def cached(cache, key=hashkey, lock=None):
    """
    Decorator to wrap a function with a memoizing callable that saves
    results in a cache.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            cache_key = key(*args, **kwargs)
            if lock:
                with lock:
                    if cache_key in cache:
                        return cache[cache_key]
                    result = func(*args, **kwargs)
                    cache[cache_key] = result
            else:
                if cache_key in cache:
                    return cache[cache_key]
                result = func(*args, **kwargs)
                cache[cache_key] = result
            return result
        return wrapper
    return decorator