def cachedmethod(cache, key=hashkey, lock=None):
    """
    यह डेकोरेटर एक क्लास या इंस्टेंस मेथड को एक मेमोराइज़िंग कॉल करने योग्य फ़ंक्शन के साथ रैप करता है, जो परिणामों को कैश में सहेजता है।
    """
    def decorator(method):
        def wrapper(self, *args, **kwargs):
            # Get cache instance - either from instance or class
            c = cache(self) if callable(cache) else cache
            
            if c is None:
                return method(self, *args, **kwargs)
                
            # Generate cache key
            k = key(self, *args, **kwargs)
            
            try:
                # Try to get cached result
                with lock or nullcontext():
                    result = c[k]
                return result
            except KeyError:
                # Calculate and cache result if not found
                result = method(self, *args, **kwargs)
                with lock or nullcontext():
                    c[k] = result
                return result
                
        return wrapper
        
    return decorator