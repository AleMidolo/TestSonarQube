def cachedmethod(cache, key=hashkey, lock=None):
    """
    Decorador para envolver un método de clase o de instancia con una función memoizadora  
    que guarda los resultados en una caché.
    """
    def decorator(method):
        def wrapper(self, *args, **kwargs):
            cache_key = key(self, *args, **kwargs)
            if lock:
                with lock:
                    if cache_key in cache:
                        return cache[cache_key]
                    result = method(self, *args, **kwargs)
                    cache[cache_key] = result
                    return result
            else:
                if cache_key in cache:
                    return cache[cache_key]
                result = method(self, *args, **kwargs)
                cache[cache_key] = result
                return result
        return wrapper
    return decorator