def cached(cache, key=hashkey, lock=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            cache_key = key(*args, **kwargs)
            if cache_key in cache:
                return cache[cache_key]
            with (lock if lock else dummy_lock):
                if cache_key not in cache:
                    result = func(*args, **kwargs)
                    cache[cache_key] = result
            return cache[cache_key]
        return wrapper
    return decorator