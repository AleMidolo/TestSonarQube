def cachedmethod(cache, key=hashkey, lock=None):
    """
    यह डेकोरेटर एक क्लास या इंस्टेंस मेथड को एक मेमोराइज़िंग कॉल करने योग्य फ़ंक्शन के साथ रैप करता है, जो परिणामों को कैश में सहेजता है।
    """
    def decorator(method):
        def wrapper(self, *args, **kwargs):
            # Get the cache instance
            c = cache(self)
            if c is None:
                return method(self, *args, **kwargs)
                
            # Generate cache key
            k = key(args, kwargs)
            
            try:
                # Try to get cached result
                with lock(self) if lock is not None else nullcontext():
                    result = c[k]
                return result
            except KeyError:
                # Cache miss - call method and store result
                result = method(self, *args, **kwargs)
                with lock(self) if lock is not None else nullcontext():
                    c[k] = result
                return result
                
        return wrapper
        
    return decorator