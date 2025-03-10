from functools import wraps
from collections import defaultdict, OrderedDict

def lfu_cache(maxsize=128, typed=False):
    def decorator(func):
        cache = {}
        freq = defaultdict(OrderedDict)
        min_freq = 0

        @wraps(func)
        def wrapper(*args, **kwargs):
            if typed:
                key = (args, tuple(sorted(kwargs.items())))
            else:
                key = args + tuple(sorted(kwargs.items()))
            
            if key in cache:
                # Increment the frequency of the key
                freq_val = cache[key][1]
                freq[freq_val].pop(key)
                if not freq[freq_val]:
                    if freq_val == min_freq:
                        min_freq += 1
                    del freq[freq_val]
                cache[key][1] += 1
                freq[cache[key][1]][key] = None
                return cache[key][0]
            
            result = func(*args, **kwargs)
            
            if len(cache) >= maxsize:
                # Remove the least frequently used item
                evict_key = freq[min_freq].popitem(last=False)[0]
                del cache[evict_key]
            
            cache[key] = [result, 1]
            freq[1][key] = None
            min_freq = 1
            return result
        
        return wrapper
    return decorator