def cachedmethod(cache, key=hashkey, lock=None):
    """
    Decorator per racchiudere un metodo di classe o di istanza con una funzione memoizzante che salva i risultati in una cache.
    """
    def decorator(func):
        def wrapper(self, *args, **kwargs):
            # Generate the cache key based on the provided key function
            cache_key = key(self, *args, **kwargs)
            # Acquire lock if provided
            if lock:
                with lock:
                    if cache_key not in cache:
                        cache[cache_key] = func(self, *args, **kwargs)
                    return cache[cache_key]
            else:
                if cache_key not in cache:
                    cache[cache_key] = func(self, *args, **kwargs)
                return cache[cache_key]
        return wrapper
    return decorator