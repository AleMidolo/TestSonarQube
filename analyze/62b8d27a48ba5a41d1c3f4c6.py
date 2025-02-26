def cached(cache, key=hashkey, lock=None):
    """
    यह एक डेकोरेटर है जो किसी फ़ंक्शन को एक मेमोराइज़िंग कॉल करने योग्य (memoizing callable) के साथ रैप करता है, जो परिणामों को कैश में सहेजता है।
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Create a unique cache key based on the function arguments
            cache_key = key(*args, **kwargs)
            if cache_key in cache:
                return cache[cache_key]
            with (lock if lock else dummy_lock):
                if cache_key not in cache:  # Double-check in case another thread added it
                    cache[cache_key] = func(*args, **kwargs)
            return cache[cache_key]
        return wrapper
    return decorator