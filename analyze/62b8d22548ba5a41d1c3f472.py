def cachedmethod(cache, key=hashkey, lock=None):
    """
    Decorator to wrap a class or instance method with a memoizing
    callable that saves results in a cache.
    """
    def decorator(method):
        def wrapper(self, *args, **kwargs):
            cache_key = key(self, *args, **kwargs)
            if lock is not None:
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