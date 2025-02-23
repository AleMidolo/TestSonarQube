def cachedmethod(cache, key=hashkey, lock=None):
    """
    Decorator per racchiudere un metodo di classe o di istanza con una funzione memoizzante che salva i risultati in una cache.
    """
    def decorator(func):
        def wrapper(self, *args, **kwargs):
            # Generate the cache key
            cache_key = key(self, *args, **kwargs)
            # Acquire lock if provided
            if lock:
                with lock:
                    if cache_key in cache:
                        return cache[cache_key]
                    result = func(self, *args, **kwargs)
                    cache[cache_key] = result
                    return result
            else:
                if cache_key in cache:
                    return cache[cache_key]
                result = func(self, *args, **kwargs)
                cache[cache_key] = result
                return result
        return wrapper
    return decorator