from collections import OrderedDict
from functools import wraps

def mru_cache(maxsize=128, typed=False):
    """ 
    एक डेकोरेटर जो एक फ़ंक्शन को एक मेमोराइज़िंग कॉलेबल के साथ रैप करता है,
    जो 'Most Recently Used' (MRU) एल्गोरिदम के आधार पर अधिकतम `maxsize` 
    परिणामों को सहेजता है।
    """
    def decorator(func):
        cache = OrderedDict()

        @wraps(func)
        def wrapper(*args, **kwargs):
            key = (args, frozenset(kwargs.items())) if typed else args
            if key in cache:
                cache.move_to_end(key)
                return cache[key]
            result = func(*args, **kwargs)
            cache[key] = result
            if len(cache) > maxsize:
                cache.popitem(last=False)
            return result

        return wrapper

    return decorator