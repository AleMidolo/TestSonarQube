from functools import lru_cache as _lru_cache

def lru_cache(maxsize=128, typed=False):
    """
    一个用于将函数包装为一个带有记忆功能的可调用对象的装饰器，
    该对象基于最近最少使用（LRU）算法保存，最多 `maxsize` 个结果。
    """
    def decorator(func):
        return _lru_cache(maxsize=maxsize, typed=typed)(func)
    return decorator