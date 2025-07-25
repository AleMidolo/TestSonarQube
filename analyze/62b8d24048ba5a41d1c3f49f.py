from functools import wraps
from collections import OrderedDict
import time

def ttl_cache(maxsize=128, ttl=600, timer=time.monotonic, typed=False):
    """
    一个用于将函数包装为一个带有缓存功能的可调用对象的装饰器。
    该缓存基于最近最少使用（LRU）算法，最多保存 `maxsize` 个结果，
    并为每个缓存项设置一个生存时间（TTL，单位为秒）。
    """
    def decorator(func):
        # 使用OrderedDict存储缓存,保持插入顺序
        cache = OrderedDict()
        
        # 生成缓存键的函数
        def make_key(args, kwargs):
            key = (args, frozenset(kwargs.items()))
            if typed:
                key += tuple(type(arg) for arg in args)
                key += tuple(type(val) for val in kwargs.values())
            return hash(key)
        
        @wraps(func)
        def wrapper(*args, **kwargs):
            key = make_key(args, kwargs)
            
            # 检查是否在缓存中且未过期
            if key in cache:
                result, timestamp = cache[key]
                if timer() - timestamp <= ttl:
                    # 将访问的项移到末尾(最近使用)
                    cache.move_to_end(key)
                    return result
                else:
                    # 过期则删除
                    del cache[key]
            
            # 计算新结果
            result = func(*args, **kwargs)
            
            # 添加到缓存
            cache[key] = (result, timer())
            
            # 如果超过最大大小，删除最早的项
            if maxsize and len(cache) > maxsize:
                cache.popitem(last=False)
                
            return result
            
        # 添加缓存清理方法
        def clear_cache():
            cache.clear()
            
        wrapper.clear_cache = clear_cache
        return wrapper
        
    return decorator