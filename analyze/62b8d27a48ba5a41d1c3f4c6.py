def cached(cache, key=hashkey, lock=None):
    """
    यह एक डेकोरेटर है जो किसी फ़ंक्शन को एक मेमोराइज़िंग कॉल करने योग्य (memoizing callable) के साथ रैप करता है, जो परिणामों को कैश में सहेजता है।
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            k = key(*args, **kwargs)
            
            try:
                return cache[k]
            except KeyError:
                pass
                
            if lock is not None:
                with lock:
                    if k in cache:
                        return cache[k]
                    result = func(*args, **kwargs)
                    cache[k] = result
                    return result
            else:
                result = func(*args, **kwargs)
                cache[k] = result
                return result
                
        return wrapper
    return decorator