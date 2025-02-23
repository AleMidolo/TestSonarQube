from collections import defaultdict, OrderedDict
import functools

def lfu_cache(maxsize=128, typed=False):
    """
    Decorator to wrap a function with a memoizing callable that saves
    up to `maxsize` results based on a Least Frequently Used (LFU)
    algorithm.
    """
    def decorator(func):
        cache = {}
        frequency = defaultdict(int)
        order = OrderedDict()
        
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            key = (args, frozenset(kwargs.items())) if typed else args
            if key in cache:
                frequency[key] += 1
                order.move_to_end(key)
                return cache[key]
            result = func(*args, **kwargs)
            if len(cache) >= maxsize:
                lfu_key = min(order, key=lambda k: frequency[k])
                cache.pop(lfu_key)
                frequency.pop(lfu_key)
                order.pop(lfu_key)
            cache[key] = result
            frequency[key] = 1
            order[key] = None
            return result
        
        return wrapper
    
    return decorator