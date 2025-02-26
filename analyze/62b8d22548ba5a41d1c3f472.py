def cachedmethod(cache, key=hashkey, lock=None):
    """
    यह डेकोरेटर एक क्लास या इंस्टेंस मेथड को एक मेमोराइज़िंग कॉल करने योग्य फ़ंक्शन के साथ रैप करता है, जो परिणामों को कैश में सहेजता है।
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Generate the cache key
            cache_key = key(*args, **kwargs)
            # Check if the result is in the cache
            if cache_key in cache:
                return cache[cache_key]
            # Acquire lock if provided
            if lock:
                with lock:
                    # Check again in case another thread has computed it
                    if cache_key in cache:
                        return cache[cache_key]
                    # Call the function and cache the result
                    result = func(*args, **kwargs)
                    cache[cache_key] = result
                    return result
            else:
                # Call the function and cache the result
                result = func(*args, **kwargs)
                cache[cache_key] = result
                return result
        return wrapper
    return decorator