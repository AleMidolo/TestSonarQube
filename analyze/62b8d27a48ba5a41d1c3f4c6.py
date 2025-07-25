def cached(cache, key=hashkey, lock=None):
    """
    Decorador para envolver una función con una llamada que memoriza y guarda  
    los resultados en una caché.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            k = key(*args, **kwargs)
            
            try:
                return cache[k]
            except KeyError:
                pass
            
            if lock is not None:
                with lock:
                    try:
                        return cache[k]
                    except KeyError:
                        v = func(*args, **kwargs)
                        cache[k] = v
                        return v
            
            v = func(*args, **kwargs)
            cache[k] = v
            return v
            
        return wrapper
    return decorator