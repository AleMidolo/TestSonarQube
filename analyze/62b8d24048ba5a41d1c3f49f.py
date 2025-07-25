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
        # 使用OrderedDict来实现LRU缓存
        cache = OrderedDict()
        # 存储缓存项的过期时间
        expires = OrderedDict()
        
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
            now = timer()
            
            # 检查是否在缓存中且未过期
            if key in cache:
                if now < expires[key]:
                    # 将访问的项移到OrderedDict末尾
                    cache.move_to_end(key)
                    expires.move_to_end(key)
                    return cache[key]
                else:
                    # 删除过期项
                    del cache[key]
                    del expires[key]
            
            # 计算新值
            result = func(*args, **kwargs)
            
            # 如果缓存已满，删除最早的项
            if maxsize > 0:
                while len(cache) >= maxsize:
                    cache.popitem(last=False)
                    expires.popitem(last=False)
                
                # 添加新项到缓存
                cache[key] = result
                expires[key] = now + ttl
            
            return result
            
        # 添加清除缓存的方法
        def clear_cache():
            cache.clear()
            expires.clear()
            
        wrapper.clear_cache = clear_cache
        return wrapper
        
    return decorator