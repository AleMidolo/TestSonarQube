from functools import wraps

def cached(cache, key=hashkey, lock=None):
    """
    Decorador para envolver una función con una llamada que memoriza y guarda  
    los resultados en una caché.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            cache_key = key(*args, **kwargs)
            if lock:
                with lock:
                    if cache_key in cache:
                        return cache[cache_key]
                    result = func(*args, **kwargs)
                    cache[cache_key] = result
            else:
                if cache_key in cache:
                    return cache[cache_key]
                result = func(*args, **kwargs)
                cache[cache_key] = result
            return result
        return wrapper
    return decorator