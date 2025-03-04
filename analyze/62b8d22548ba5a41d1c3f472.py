def cachedmethod(cache, key=hashkey, lock=None):
    """
    Decorator to wrap a class or instance method with a memoizing
    callable that saves results in a cache.
    """
    def decorator(method):
        def wrapper(self, *args, **kwargs):
            # Get cache instance
            _cache = cache(self) if callable(cache) else cache
            
            # Generate cache key
            k = key(method, args, kwargs)
            
            try:
                # Try to get cached result
                if lock is not None:
                    with lock:
                        result = _cache[k]
                else:
                    result = _cache[k]
                return result
            
            except KeyError:
                # Cache miss - call method and store result
                result = method(self, *args, **kwargs)
                
                if lock is not None:
                    with lock:
                        _cache[k] = result
                else:
                    _cache[k] = result
                    
                return result
                
        return wrapper
        
    return decorator