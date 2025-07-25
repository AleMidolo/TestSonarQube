def cached(cache, key=hashkey, lock=None):
    """
    Decorator per racchiudere una funzione con un callable di memoizzazione che salva
    i risultati in una cache.
    """
    def decorator(function):
        def wrapper(*args, **kwargs):
            k = key(*args, **kwargs)
            
            try:
                # Try to get result from cache
                result = cache[k]
            except KeyError:
                # If not in cache, compute and store result
                if lock is not None:
                    with lock:
                        result = function(*args, **kwargs)
                        cache[k] = result
                else:
                    result = function(*args, **kwargs)
                    cache[k] = result
                    
            return result
            
        wrapper.__doc__ = function.__doc__
        wrapper.__name__ = function.__name__
        return wrapper
        
    return decorator