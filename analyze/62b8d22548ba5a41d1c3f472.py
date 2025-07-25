def cachedmethod(cache, key=hashkey, lock=None):
    """
    Decorator per racchiudere un metodo di classe o di istanza con una funzione memoizzante 
    che salva i risultati in una cache.
    """
    def decorator(method):
        def wrapper(self, *args, **kwargs):
            # Get cache instance
            cache_instance = cache(self) if callable(cache) else cache
            
            # Generate key
            k = key(method, args, kwargs)
            
            try:
                # Try to get result from cache
                if lock is not None:
                    with lock:
                        result = cache_instance[k]
                else:
                    result = cache_instance[k]
                return result
            
            except KeyError:
                # If not in cache, compute and store result
                result = method(self, *args, **kwargs)
                if lock is not None:
                    with lock:
                        cache_instance[k] = result
                else:
                    cache_instance[k] = result
                return result
                
        return wrapper
        
    return decorator