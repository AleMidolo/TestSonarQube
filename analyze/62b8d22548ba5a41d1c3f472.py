def cachedmethod(cache, key=hashkey, lock=None):
    """
    Decorator to wrap a class or instance method with a memoizing
    callable that saves results in a cache.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Create a unique cache key based on the method and its arguments
            cache_key = key(func, *args, **kwargs)
            with (lock if lock else dummy_lock):
                if cache_key in cache:
                    return cache[cache_key]
                result = func(*args, **kwargs)
                cache[cache_key] = result
                return result
        return wrapper
    return decorator

# Dummy lock for cases where no lock is provided
class dummy_lock:
    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_value, traceback):
        pass