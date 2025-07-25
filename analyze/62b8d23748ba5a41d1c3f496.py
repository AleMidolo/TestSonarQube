from functools import wraps
from collections import defaultdict, OrderedDict

def lfu_cache(maxsize=128, typed=False):
    def decorator(func):
        cache = {}
        frequency = defaultdict(OrderedDict)
        min_freq = 0

        @wraps(func)
        def wrapper(*args, **kwargs):
            if typed:
                key = (args, tuple(sorted(kwargs.items())))
            else:
                key = args + tuple(sorted(kwargs.items()))

            if key in cache:
                # Increment frequency and move to the next frequency level
                freq = cache[key][1]
                frequency[freq].pop(key)
                if not frequency[freq]:
                    if freq == min_freq:
                        min_freq += 1
                    del frequency[freq]
                cache[key][1] += 1
                frequency[cache[key][1]][key] = None
                return cache[key][0]
            
            result = func(*args, **kwargs)
            
            if len(cache) >= maxsize:
                # Remove the least frequently used item
                evict_key, _ = frequency[min_freq].popitem(last=False)
                if not frequency[min_freq]:
                    del frequency[min_freq]
                del cache[evict_key]
            
            cache[key] = [result, 1]
            frequency[1][key] = None
            min_freq = 1
            
            return result
        
        return wrapper
    
    return decorator