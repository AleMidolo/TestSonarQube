from collections import defaultdict
from functools import wraps

def lfu_cache(maxsize=128, typed=False):
    """
    Decorator to wrap a function with a memoizing callable that saves
    up to `maxsize` results based on a Least Frequently Used (LFU)
    algorithm.
    """
    cache = {}
    usage_count = defaultdict(int)

    @wraps(func)
    def wrapper(*args, **kwargs):
        key = args if not typed else (args, frozenset(kwargs.items()))
        if key in cache:
            usage_count[key] += 1
            return cache[key]
        
        result = func(*args, **kwargs)
        if len(cache) >= maxsize:
            lfu_key = min(usage_count, key=usage_count.get)
            del cache[lfu_key]
            del usage_count[lfu_key]
        
        cache[key] = result
        usage_count[key] += 1
        return result

    return wrapper