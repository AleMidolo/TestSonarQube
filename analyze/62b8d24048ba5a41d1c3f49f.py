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
            if typed:
                key = (args, frozenset(kwargs.items()))
            else:
                key = (tuple(args), frozenset(kwargs.items()))

            current_time = timer()
            if key in cache:
                if current_time - timestamps[key] < ttl:
                    # Move to end to show that it was recently used
                    cache.move_to_end(key)
                    return cache[key]
                else:
                    # Remove expired item
                    del cache[key]
                    del timestamps[key]

            # Call the function and cache the result
            result = func(*args, **kwargs)
            cache[key] = result
            timestamps[key] = current_time

            # Maintain the cache size
            if len(cache) > maxsize:
                cache.popitem(last=False)
                timestamps.popitem(last=False)

            return result

        return wrapper

    return decorator