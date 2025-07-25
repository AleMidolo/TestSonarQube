from collections import defaultdict
from functools import wraps

def lfu_cache(maxsize=128, typed=False):
    """
    Decorator to wrap a function with a memoizing callable that saves
    up to `maxsize` results based on a Least Frequently Used (LFU)
    algorithm.
    """
    cache = {}
    frequency = defaultdict(int)
    order = []

    @wraps(func)
    def wrapper(*args, **kwargs):
        key = args if not typed else (args, frozenset(kwargs.items()))
        if key in cache:
            frequency[key] += 1
            return cache[key]
        
        result = func(*args, **kwargs)
        if len(cache) >= maxsize:
            lfu_key = min(order, key=lambda k: frequency[k])
            del cache[lfu_key]
            order.remove(lfu_key)
        
        cache[key] = result
        frequency[key] += 1
        order.append(key)
        return result

    return wrapper