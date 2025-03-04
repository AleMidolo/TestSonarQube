def cachedmethod(cache, key=hashkey, lock=None):
    """
    返回一个装饰器函数，可以调用缓存中的结果。
    该装饰器用于包装类方法或实例方法，使其成为一个具备记忆功能的可调用对象，并将结果存储在缓存中。
    """
    def decorator(method):
        def wrapper(self, *args, **kwargs):
            # 生成缓存键
            cache_key = key(self, *args, **kwargs)
            
            # 如果指定了锁,则加锁访问缓存
            if lock is not None:
                with lock:
                    if cache_key in cache:
                        return cache[cache_key]
                    result = method(self, *args, **kwargs)
                    cache[cache_key] = result
                    return result
            
            # 无锁访问缓存
            if cache_key in cache:
                return cache[cache_key]
                
            result = method(self, *args, **kwargs)
            cache[cache_key] = result
            return result
            
        # 保留原方法的元数据
        wrapper.__doc__ = method.__doc__
        wrapper.__name__ = method.__name__
        
        return wrapper
    return decorator