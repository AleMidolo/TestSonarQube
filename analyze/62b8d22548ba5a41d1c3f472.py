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
            # Acquire lock if provided
            if lock:
                with lock:
                    # Check again in case another thread has computed the value
                    if cache_key in cache:
                        return cache[cache_key]
                    # Compute the value
                    result = func(self, *args, **kwargs)
                    # Store the result in the cache
                    cache[cache_key] = result
                    return result
            else:
                # Compute the value
                result = func(self, *args, **kwargs)
                # Store the result in the cache
                cache[cache_key] = result
                return result
        return wrapper
    return decorator