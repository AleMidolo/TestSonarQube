from collections import defaultdict, OrderedDict
import functools

def lfu_cache(maxsize=128, typed=False):
    """
    एक डेकोरेटर जो एक फ़ंक्शन को एक मेमोराइज़िंग कॉल करने योग्य (memoizing callable) के साथ रैप करता है,
    जो `maxsize` तक के परिणामों को Least Frequently Used (LFU) एल्गोरिदम के आधार पर सहेजता है।
    """
    def decorator(func):
        cache = {}
        frequency = defaultdict(int)
        order = OrderedDict()
        
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if typed:
                key = (args, frozenset(kwargs.items()))
            else:
                key = (tuple(args), frozenset(kwargs.items()))
                
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