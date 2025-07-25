def cached(cache, key=hashkey, lock=None):
    """
    Decorator per racchiudere una funzione con un callable di memoizzazione che salva
    i risultati in una cache.
    """
    def decorator(function):
        def wrapper(*args, **kwargs):
            k = key(*args, **kwargs)
            
            try:
                result = cache[k]
            except KeyError:
                if lock is not None:
                    with lock:
                        try:
                            result = cache[k]
                        except KeyError:
                            result = function(*args, **kwargs)
                            cache[k] = result
                else:
                    result = function(*args, **kwargs)
                    cache[k] = result
                    
            return result
            
        return wrapper
        
    return decorator