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
            # 如果考虑类型,将参数转换为包含类型的key
            if typed:
                key = (args, tuple(sorted(kwargs.items())), 
                      tuple(type(arg) for arg in args),
                      tuple(type(val) for val in kwargs.values()))
            else:
                key = (args, tuple(sorted(kwargs.items())))
                
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
                
            # 存储新结果
            cache[key] = result
            access_order.append(key)
            
            return result
            
        # 添加缓存信息的访问方法
        wrapper.cache_info = lambda: {
            'hits': len(access_order),
            'maxsize': maxsize,
            'currsize': len(cache)
        }
        wrapper.cache_clear = lambda: cache.clear() and access_order.clear()
        
        return wrapper
        
    # 如果maxsize为None,则不使用缓存
    if maxsize is None:
        return lambda func: func
        
    # 确保maxsize为整数
    maxsize = int(maxsize)
    if maxsize < 0:
        raise ValueError('maxsize must be non-negative')
        
    return decorator