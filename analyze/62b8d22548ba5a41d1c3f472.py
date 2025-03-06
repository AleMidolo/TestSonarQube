def cachedmethod(cache, key=hashkey, lock=None):
    """
    返回一个装饰器函数，可以调用缓存中的结果。
    该装饰器用于包装类方法或实例方法，使其成为一个具备记忆功能的可调用对象，并将结果存储在缓存中。
    """
    def decorator(method):
        def wrapper(self, *args, **kwargs):
            cache_key = key(self, *args, **kwargs)
            if lock:
                with lock:
                    if cache_key in cache:
                        return cache[cache_key]
                    result = method(self, *args, **kwargs)
                    cache[cache_key] = result
                    return result
            else:
                if cache_key in cache:
                    return cache[cache_key]
                result = method(self, *args, **kwargs)
                cache[cache_key] = result
                return result
        return wrapper
    return decorator