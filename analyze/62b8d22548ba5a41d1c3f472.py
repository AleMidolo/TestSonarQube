def cachedmethod(cache, key=hashkey, lock=None):
    """
    Decorator per racchiudere un metodo di classe o di istanza con una funzione memoizzante che salva i risultati in una cache.
    """
    def decorator(func):
        def wrapper(self, *args, **kwargs):
            # Generate the cache key
            cache_key = key(self, *args, **kwargs)
            # Check if the result is in the cache
            if cache_key in cache:
                return cache[cache_key]
            # If not, call the function and store the result in the cache
            with (lock if lock else dummy_lock):
                result = func(self, *args, **kwargs)
                cache[cache_key] = result
            return result
        return wrapper
    return decorator

# Dummy lock for cases where no lock is provided
class dummy_lock:
    def __enter__(self):
        pass
    def __exit__(self, *args):
        pass