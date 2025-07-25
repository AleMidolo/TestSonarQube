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
                    if k in cache:
                        return cache[k]
                    result = func(*args, **kwargs)
                    cache[k] = result
            else:
                result = func(*args, **kwargs)
                cache[k] = result
                
            return result
            
        return wrapper
    return decorator