def cachedmethod(cache, key=hashkey, lock=None):
    """
    Decorator per racchiudere un metodo di classe o di istanza con una funzione memoizzante che salva i risultati in una cache.
    """
    def decorator(func):
        def wrapper(self, *args, **kwargs):
            if lock:
                with lock:
                    cache_key = key(self, *args, **kwargs)
                    if cache_key in cache:
                        return cache[cache_key]
                    result = func(self, *args, **kwargs)
                    cache[cache_key] = result
                    return result
            else:
                cache_key = key(self, *args, **kwargs)
                if cache_key in cache:
                    return cache[cache_key]
                result = func(self, *args, **kwargs)
                cache[cache_key] = result
                return result
        return wrapper
    return decorator