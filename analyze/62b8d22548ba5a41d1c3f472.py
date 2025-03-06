def cachedmethod(cache, key=hashkey, lock=None):
    """
    यह डेकोरेटर एक क्लास या इंस्टेंस मेथड को एक मेमोराइज़िंग कॉल करने योग्य फ़ंक्शन के साथ रैप करता है, जो परिणामों को कैश में सहेजता है।
    """
    def decorator(method):
        def wrapper(self, *args, **kwargs):
            cache_key = key(self, *args, **kwargs)
            if lock:
                with lock:
                    if cache_key in cache:
                        return cache[cache_key]
                    result = method(self, *args, **kwargs)
                    cache[cache_key] = result
                    return result
            else:
                if cache_key in cache:
                    return cache[cache_key]
                result = method(self, *args, **kwargs)
                cache[cache_key] = result
                return result
        return wrapper
    return decorator