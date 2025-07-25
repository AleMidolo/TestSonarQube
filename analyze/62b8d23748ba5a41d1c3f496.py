from collections import defaultdict, OrderedDict
import functools

def lfu_cache(maxsize=128, typed=False):
    """
    一个用于将函数包装为一个带有记忆功能的可调用对象的装饰器，
    该对象基于最少使用频率（LFU，Least Frequently Used）算法，
    保存最多 `maxsize` 个结果。
    """
    def decorator(func):
        cache = {}
        freq = defaultdict(int)
        order = OrderedDict()
        
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            key = (args, frozenset(kwargs.items())) if typed else args
            if key in cache:
                freq[key] += 1
                order.move_to_end(key)
                return cache[key]
            result = func(*args, **kwargs)
            if len(cache) >= maxsize:
                lfu_key = min(order, key=lambda k: (freq[k], order[k]))
                del cache[lfu_key]
                del freq[lfu_key]
                del order[lfu_key]
            cache[key] = result
            freq[key] += 1
            order[key] = None
            return result
        
        return wrapper
    
    return decorator