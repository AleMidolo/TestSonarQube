def cached(cache, key=hashkey, lock=None):
    """
    返回一个装饰器函数，将结果保存到缓存中
    一个用于包装一个函数，通过一个支持记忆功能的可调用对象将结果保存到缓存中的装饰器。
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            # 生成缓存键
            cache_key = key(*args, **kwargs)
            # 尝试从缓存中获取结果
            if cache_key in cache:
                return cache[cache_key]
            # 如果缓存中没有，调用原函数
            result = func(*args, **kwargs)
            # 将结果存入缓存
            cache[cache_key] = result
            return result
        return wrapper
    return decorator