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
            key = args if not typed else (args, frozenset(kwargs.items()))
            if key in cache:
                frequency[key] += 1
                order.move_to_end(key)
                return cache[key]
            result = func(*args, **kwargs)
            cache[key] = result
            frequency[key] += 1
            order[key] = frequency[key]
            if len(cache) > maxsize:
                lfu_key = min(order, key=order.get)
                del cache[lfu_key]
                del frequency[lfu_key]
                del order[lfu_key]
            return result
        
        return wrapper
    
    return decorator