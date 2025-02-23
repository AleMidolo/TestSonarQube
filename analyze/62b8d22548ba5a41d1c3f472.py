def cachedmethod(cache, key=hashkey, lock=None):
    """
    返回一个装饰器函数，可以调用缓存中的结果。
    该装饰器用于包装类方法或实例方法，使其成为一个具备记忆功能的可调用对象，并将结果存储在缓存中。
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            # 生成缓存键
            cache_key = key(args, kwargs)
            # 检查缓存
            if cache_key in cache:
                return cache[cache_key]
            # 获取结果并存储到缓存
            result = func(*args, **kwargs)
            cache[cache_key] = result
            return result
        return wrapper
    return decorator