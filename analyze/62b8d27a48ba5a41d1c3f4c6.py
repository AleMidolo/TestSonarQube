def cached(cache, key=hashkey, lock=None):
    """
    返回一个装饰器函数，将结果保存到缓存中
    一个用于包装一个函数，通过一个支持记忆功能的可调用对象将结果保存到缓存中的装饰器。
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            k = key(*args, **kwargs)
            
            try:
                # 尝试从缓存中获取结果
                result = cache[k]
                return result
            except KeyError:
                # 如果缓存中没有，则执行函数
                if lock:
                    with lock:
                        result = func(*args, **kwargs)
                        cache[k] = result
                else:
                    result = func(*args, **kwargs)
                    cache[k] = result
                return result
                
        return wrapper
    return decorator