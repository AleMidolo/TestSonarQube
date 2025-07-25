def cached(cache, key=hashkey, lock=None):
    """
    यह एक डेकोरेटर है जो किसी फ़ंक्शन को एक मेमोराइज़िंग कॉल करने योग्य (memoizing callable) के साथ रैप करता है, जो परिणामों को कैश में सहेजता है।
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Generate the cache key
            cache_key = key(*args, **kwargs)
            # Check if the result is in the cache
            if cache_key in cache:
                return cache[cache_key]
            # If not, call the function and store the result in the cache
            with (lock if lock else dummy_lock):
                result = func(*args, **kwargs)
                cache[cache_key] = result
            return result
        return wrapper
    return decorator