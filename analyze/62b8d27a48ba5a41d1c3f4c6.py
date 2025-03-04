def cached(cache, key=hashkey, lock=None):
    """
    返回一个装饰器函数，将结果保存到缓存中
    一个用于包装一个函数，通过一个支持记忆功能的可调用对象将结果保存到缓存中的装饰器。
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            k = key(*args, **kwargs)
            
            try:
                # 如果缓存中存在结果,直接返回
                return cache[k]
            except KeyError:
                pass  # 继续执行
                
            if lock is not None:
                with lock:
                    # 双重检查,避免重复计算
                    try:
                        return cache[k]
                    except KeyError:
                        # 计算结果并缓存
                        cache[k] = result = func(*args, **kwargs)
                        return result
            else:
                # 无锁情况下直接计算并缓存
                cache[k] = result = func(*args, **kwargs)
                return result
                
        return wrapper
    return decorator