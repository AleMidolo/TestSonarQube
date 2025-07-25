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
                    # Check again in case another thread has already computed the result
                    if cache_key in cache:
                        return cache[cache_key]
                    # Compute the result
                    result = func(self, *args, **kwargs)
                    # Store the result in the cache
                    cache[cache_key] = result
                    return result
            else:
                # Compute the result
                result = func(self, *args, **kwargs)
                # Store the result in the cache
                cache[cache_key] = result
                return result
        return wrapper
    return decorator