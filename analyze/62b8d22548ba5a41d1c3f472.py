def cachedmethod(cache, key=hashkey, lock=None):
    """
    यह डेकोरेटर एक क्लास या इंस्टेंस मेथड को एक मेमोराइज़िंग कॉल करने योग्य फ़ंक्शन के साथ रैप करता है, जो परिणामों को कैश में सहेजता है।
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

# Dummy lock for cases where no lock is provided
class dummy_lock:
    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_value, traceback):
        pass