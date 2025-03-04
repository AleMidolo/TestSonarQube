def ttl_cache(maxsize=128, ttl=600, timer=time.monotonic, typed=False):
    """
    एक डेकोरेटर जो एक फ़ंक्शन को एक मेमोराइज़िंग कॉलेबल के साथ रैप करता है,
    जो `maxsize` तक के परिणामों को सेव करता है। यह एक Least Recently Used (LRU)
    एल्गोरिदम पर आधारित होता है और प्रत्येक आइटम के लिए एक समय-सीमा (Time-To-Live, TTL) 
    मान लागू करता है।
    """
    def decorator(func):
        # Create cache dict to store results and timestamps
        cache = {}
        # Create ordered dict to track LRU
        cache_order = collections.OrderedDict()
        
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Create cache key based on args
            key = args
            if typed:
                key += tuple(type(arg) for arg in args)
            if kwargs:
                key += tuple(sorted(kwargs.items()))
                if typed:
                    key += tuple(type(v) for v in kwargs.values())
            
            # Get current time
            now = timer()
            
            # Check if result in cache and not expired
            if key in cache:
                result, timestamp = cache[key]
                if now - timestamp <= ttl:
                    # Move key to end to mark as most recently used
                    cache_order.move_to_end(key)
                    return result
                else:
                    # Remove expired entry
                    del cache[key]
                    del cache_order[key]
            
            # Call function to get new result
            result = func(*args, **kwargs)
            
            # Add to cache
            cache[key] = (result, now)
            cache_order[key] = None
            
            # Remove oldest entries if cache too large
            while len(cache) > maxsize:
                oldest_key = next(iter(cache_order))
                del cache[oldest_key]
                del cache_order[oldest_key]
                
            return result
            
        # Add cache clear method
        def clear_cache():
            cache.clear()
            cache_order.clear()
            
        wrapper.clear_cache = clear_cache
        return wrapper
        
    return decorator