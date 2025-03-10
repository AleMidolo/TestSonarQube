def cached(cache, key=hashkey, lock=None):
    """
    Decorator per racchiudere una funzione con un callable di memoizzazione che salva  
    i risultati in una cache.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            cache_key = key(*args, **kwargs)
            if lock:
                with lock:
                    if cache_key in cache:
                        return cache[cache_key]
                    result = func(*args, **kwargs)
                    cache[cache_key] = result
                    return result
            else:
                if cache_key in cache:
                    return cache[cache_key]
                result = func(*args, **kwargs)
                cache[cache_key] = result
                return result
        return wrapper
    return decorator