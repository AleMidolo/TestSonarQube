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
                        return _cache[k]
                return _cache[k]
                
            except KeyError:
                # Cache miss - call method and store result
                v = method(self, *args, **kwargs)
                
                if lock is not None:
                    with lock:
                        _cache[k] = v
                else:
                    _cache[k] = v
                    
                return v
                
        wrapper.__doc__ = method.__doc__
        wrapper.__name__ = method.__name__
        return wrapper
        
    return decorator