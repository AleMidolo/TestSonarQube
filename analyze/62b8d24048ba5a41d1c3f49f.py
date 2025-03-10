import time
from functools import lru_cache, wraps

def ttl_cache(maxsize=128, ttl=600, timer=time.monotonic, typed=False):
    """
    一个用于将函数包装为一个带有缓存功能的可调用对象的装饰器。
    该缓存基于最近最少使用（LRU）算法，最多保存 `maxsize` 个结果，
    并为每个缓存项设置一个生存时间（TTL，单位为秒）。
    """
    def decorator(func):
        @lru_cache(maxsize=maxsize, typed=typed)
        def cached_func(*args, **kwargs):
            return func(*args, **kwargs)

        @wraps(func)
        def wrapper(*args, **kwargs):
            key = (args, frozenset(kwargs.items())) if kwargs else args
            if key in wrapper._cache:
                value, timestamp = wrapper._cache[key]
                if timer() - timestamp < ttl:
                    return value
            result = cached_func(*args, **kwargs)
            wrapper._cache[key] = (result, timer())
            return result

        wrapper._cache = {}
        return wrapper

    return decorator