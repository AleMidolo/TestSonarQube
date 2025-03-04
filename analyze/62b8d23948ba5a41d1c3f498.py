def lru_cache(maxsize=128, typed=False):
    """
    一个用于将函数包装为一个带有记忆功能的可调用对象的装饰器，
    该对象基于最近最少使用（LRU）算法保存，最多 `maxsize` 个结果。
    """
    def decorator(func):
        # 使用字典存储缓存结果
        cache = {}
        # 使用列表记录访问顺序
        access_order = []
        
        def wrapper(*args, **kwargs):
            # 如果考虑类型,将参数类型加入key
            if typed:
                key = (*args, *kwargs.items(), *tuple(type(arg) for arg in args))
            else:
                key = (*args, *kwargs.items())
                
            # 如果结果在缓存中
            if key in cache:
                # 更新访问顺序
                access_order.remove(key)
                access_order.append(key)
                return cache[key]
            
            # 计算新结果
            result = func(*args, **kwargs)
            
            # 如果缓存已满,删除最久未使用的项
            if len(cache) >= maxsize:
                oldest_key = access_order.pop(0)
                del cache[oldest_key]
                
            # 添加新结果到缓存
            cache[key] = result
            access_order.append(key)
            
            return result
            
        # 添加缓存信息方法
        wrapper.cache_info = lambda: {
            "hits": len(access_order),
            "maxsize": maxsize,
            "currsize": len(cache)
        }
        
        # 清除缓存方法
        wrapper.cache_clear = lambda: (cache.clear(), access_order.clear())
        
        return wrapper
        
    return decorator