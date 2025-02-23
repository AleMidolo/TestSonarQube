import time
from collections import OrderedDict
from functools import wraps

def ttl_cache(maxsize=128, ttl=600, timer=time.monotonic, typed=False):
    """
    一个用于将函数包装为一个带有缓存功能的可调用对象的装饰器。
    该缓存基于最近最少使用（LRU）算法，最多保存 `maxsize` 个结果，
    并为每个缓存项设置一个生存时间（TTL，单位为秒）。
    """
    def decorator(func):
        cache = OrderedDict()
        cache_times = {}

        @wraps(func)
        def wrapper(*args, **kwargs):
            key = args if not typed else (args, frozenset(kwargs.items()))
            current_time = timer()
            
            # Clean up expired cache entries
            if key in cache:
                if current_time - cache_times[key] < ttl:
                    return cache[key]
                else:
                    del cache[key]
                    del cache_times[key]

            # Call the function and cache the result
            result = func(*args, **kwargs)
            cache[key] = result
            cache_times[key] = current_time
            
            # Maintain the cache size
            if len(cache) > maxsize:
                cache.popitem(last=False)

            return result

        return wrapper

    return decorator