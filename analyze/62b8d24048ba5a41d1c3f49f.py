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
        timestamps = {}

        def make_key(args, kwds):
            # 生成缓存键
            key = args
            if kwds:
                key += tuple(sorted(kwds.items()))
            if typed:
                key += tuple(type(arg) for arg in args)
                if kwds:
                    key += tuple(type(v) for v in kwds.values())
            return hash(key)

        @wraps(func)
        def wrapper(*args, **kwargs):
            key = make_key(args, kwargs)
            current_time = timer()

            # 检查是否在缓存中且未过期
            if key in cache:
                if current_time - timestamps[key] < ttl:
                    # 将最近使用的项移到末尾
                    cache.move_to_end(key)
                    return cache[key]
                else:
                    # 删除过期项
                    del cache[key]
                    del timestamps[key]

            # 计算新值
            result = func(*args, **kwargs)

            # 如果缓存已满，删除最早的项
            if maxsize > 0:
                while len(cache) >= maxsize:
                    oldest = next(iter(cache))
                    del cache[oldest]
                    del timestamps[oldest]

            # 添加新项到缓存
            cache[key] = result
            timestamps[key] = current_time
            cache.move_to_end(key)

            return result

        # 添加缓存统计和清理方法
        wrapper.cache_info = lambda: {
            'maxsize': maxsize,
            'currsize': len(cache),
            'ttl': ttl
        }
        wrapper.cache_clear = lambda: (cache.clear(), timestamps.clear())

        return wrapper

    return decorator