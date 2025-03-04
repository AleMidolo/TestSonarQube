from collections import OrderedDict
from functools import wraps

def mru_cache(maxsize=128, typed=False):
    def decorator(func):
        # 使用OrderedDict来存储缓存,保持插入顺序
        cache = OrderedDict()
        
        @wraps(func)
        def wrapper(*args, **kwargs):
            # 如果typed=True,将参数类型也作为key的一部分
            if typed:
                key = (tuple(args), tuple(sorted(kwargs.items())), 
                      tuple(type(arg) for arg in args),
                      tuple(type(v) for v in kwargs.values()))
            else:
                key = (tuple(args), tuple(sorted(kwargs.items())))
                
            # 如果key在缓存中,将其移到最后(最近使用)并返回值
            if key in cache:
                cache.move_to_end(key)
                return cache[key]
                
            # 计算新的结果
            result = func(*args, **kwargs)
            
            # 如果缓存已满,删除最近最少使用的项(第一个)
            if len(cache) >= maxsize:
                cache.popitem(last=False)
                
            # 添加新结果到缓存
            cache[key] = result
            return result
            
        # 添加缓存清理方法
        def clear_cache():
            cache.clear()
        wrapper.clear_cache = clear_cache
        
        return wrapper
    return decorator