def mru_cache(maxsize=128, typed=False):
    """
    一个用于将函数包装为一个带有记忆功能的可调用对象的装饰器，
    该对象基于最近最少使用（MRU，Most Recently Used）算法，
    保存最多 `maxsize` 个结果。
    """
    from collections import OrderedDict
    from functools import wraps

    def decorator(func):
        cache = OrderedDict()

        @wraps(func)
        def wrapper(*args, **kwargs):
            key = (args, frozenset(kwargs.items())) if typed else args
            if key in cache:
                cache.move_to_end(key)
                return cache[key]
            result = func(*args, **kwargs)
            cache[key] = result
            if len(cache) > maxsize:
                cache.popitem(last=False)
            return result

        return wrapper

    return decorator