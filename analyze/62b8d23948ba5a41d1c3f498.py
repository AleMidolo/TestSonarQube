from collections import OrderedDict
from functools import wraps

def lru_cache(maxsize=128, typed=False):
    """
    एक डेकोरेटर जो एक फ़ंक्शन को एक मेमोराइज़िंग कॉलेबल के साथ रैप करता है,
    जो `maxsize` तक के परिणामों को सेव करता है। यह परिणामों को 
    Least Recently Used (LRU) एल्गोरिदम के आधार पर प्रबंधित करता है।
    """
    def decorator(func):
        cache = OrderedDict()

        @wraps(func)
        def wrapper(*args):
            if typed:
                key = args
            else:
                key = tuple(map(repr, args))

            if key in cache:
                cache.move_to_end(key)
                return cache[key]
            result = func(*args)
            cache[key] = result
            if len(cache) > maxsize:
                cache.popitem(last=False)
            return result

        wrapper.cache_clear = cache.clear
        wrapper.cache_info = lambda: (len(cache), maxsize)
        return wrapper

    return decorator