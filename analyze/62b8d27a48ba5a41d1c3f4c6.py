def cached(cache, key=hashkey, lock=None):
    """
    返回一个装饰器函数，将结果保存到缓存中
    一个用于包装一个函数，通过一个支持记忆功能的可调用对象将结果保存到缓存中的装饰器。
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            cache_key = key(*args, **kwargs)
            if cache_key in cache:
                return cache[cache_key]
            if lock:
                with lock:
                    if cache_key in cache:
                        return cache[cache_key]
                    result = func(*args, **kwargs)
                    cache[cache_key] = result
                    return result
            else:
                result = func(*args, **kwargs)
                cache[cache_key] = result
                return result
        return wrapper
    return decorator