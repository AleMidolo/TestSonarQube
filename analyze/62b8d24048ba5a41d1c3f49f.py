import time
from collections import OrderedDict
from functools import wraps

def ttl_cache(maxsize=128, ttl=600, timer=time.monotonic, typed=False):
    """
    एक डेकोरेटर जो एक फ़ंक्शन को एक मेमोराइज़िंग कॉलेबल के साथ रैप करता है,
    जो `maxsize` तक के परिणामों को सेव करता है। यह एक Least Recently Used (LRU)
    एल्गोरिदम पर आधारित होता है और प्रत्येक आइटम के लिए एक समय-सीमा (Time-To-Live, TTL) 
    मान लागू करता है।
    """
    def decorator(func):
        cache = OrderedDict()
        timestamps = {}

        @wraps(func)
        def wrapper(*args, **kwargs):
            key = args if not typed else (type(args),) + args
            if key in cache:
                if timer() - timestamps[key] < ttl:
                    return cache[key]
                else:
                    del cache[key]
                    del timestamps[key]
            result = func(*args, **kwargs)
            cache[key] = result
            timestamps[key] = timer()
            if len(cache) > maxsize:
                cache.popitem(last=False)
            return result

        return wrapper

    return decorator