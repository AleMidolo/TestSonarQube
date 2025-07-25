import time
from functools import wraps, lru_cache

def ttl_cache(maxsize=128, ttl=600, timer=time.monotonic, typed=False):
    """
    एक डेकोरेटर जो एक फ़ंक्शन को एक मेमोराइज़िंग कॉलेबल के साथ रैप करता है,
    जो `maxsize` तक के परिणामों को सेव करता है। यह एक Least Recently Used (LRU)
    एल्गोरिदम पर आधारित होता है और प्रत्येक आइटम के लिए एक समय-सीमा (Time-To-Live, TTL) 
    मान लागू करता है।
    """
    def decorator(func):
        @lru_cache(maxsize=maxsize, typed=typed)
        def cached_func(*args, **kwargs):
            return func(*args, **kwargs)

        @wraps(func)
        def wrapper(*args, **kwargs):
            key = (args, frozenset(kwargs.items())) if typed else (args, tuple(kwargs.items()))
            if key in wrapper._cache:
                value, timestamp = wrapper._cache[key]
                if timer() - timestamp < ttl:
                    return value
            result = cached_func(*args, **kwargs)
            wrapper._cache[key] = (result, timer())
            return result

        wrapper._cache = {}
        return wrapper

    return decorator